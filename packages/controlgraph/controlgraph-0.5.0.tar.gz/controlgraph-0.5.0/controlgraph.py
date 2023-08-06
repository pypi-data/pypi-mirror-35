"""Generate build order graph from directory of debian packaging repositories"""

__version__ = "0.5.0"

import argparse
import logging
import re
import sys

from collections import namedtuple
from pathlib import Path
from typing import Dict, List

import networkx as nx

from debian import deb822

L = logging.getLogger("controlgraph")
L.addHandler(logging.NullHandler())


BinaryPackage = namedtuple("BinaryPackage", ["name", "source", "build_deps"])


def parse_controlfile(path: Path) -> Dict[str, BinaryPackage]:
    """Parse control file and return map of binary packages to BinaryPackages"""
    source = ""
    build_deps = []
    pkgs = {}
    with path.open() as control:
        for src in deb822.Sources.iter_paragraphs(control):
            if "Source" in src:
                source = src["Source"]
                build_deps.extend(
                    [
                        re.sub(r" \([^\)]*\)", "", s.strip()).strip()
                        for s in src["Build-Depends"].split(",")
                    ]
                )
            elif "Package" in src:
                if source != "":
                    pkgs[src["Package"]] = BinaryPackage(
                        src["Package"], source, build_deps
                    )
                else:
                    pkgs[src["Package"]] = BinaryPackage(
                        src["Package"], src["Package"], build_deps
                    )
    return pkgs


def graph(dirs: List[Path]) -> nx.DiGraph:
    """Prints linear or dot graph build order."""
    # Get dict matching binary packages to source packages/build deps
    pkgs = {}
    for path in dirs:
        controlfile = Path(path / "debian/control")
        if not controlfile.exists():
            continue
        pkgs.update(parse_controlfile(controlfile))

    # Get dict matching source package to build deps
    build_deps = {v.source: v.build_deps for _, v in pkgs.items()}
    # Get dict matching binary package to source package
    src_pkgs = {v.name: v.source for _, v in pkgs.items()}

    # Convert binary build deps to source packages (if available locally)
    for repo in build_deps:
        src_deps = []
        for dep in build_deps[repo]:
            if dep in src_pkgs:
                src_deps.append(src_pkgs[dep])
        build_deps[repo] = src_deps

    # Create graph from build deps
    dep_graph = nx.DiGraph()
    for src, deps in build_deps.items():
        dep_graph.add_node(src)
        dep_graph.add_nodes_from(deps)
        for dep in deps:
            dep_graph.add_edge(src, dep)

    return dep_graph


def main() -> int:
    """Parse args, generate graph, and print it"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version", "-V", action="store_true", help="print program version"
    )
    parser.add_argument(
        "--verbose", "-v", help="-v for info, -vv for debug", action="count", default=0
    )
    parser.add_argument(
        "--danglers-first",
        action="store_true",
        help="list all independent repositories first",
    )
    parser.add_argument(
        "--danglers-only",
        action="store_true",
        help="only list independent repositories",
    )
    parser.add_argument(
        "--no-danglers",
        action="store_true",
        help="drop all independent repositories from graph",
    )
    parser.add_argument(
        "directories", type=Path, nargs="*", help="directories to graph"
    )
    group_graph_type = parser.add_mutually_exclusive_group()
    group_graph_type.add_argument(
        "--linear",
        "-l",
        dest="linear",
        action="store_true",
        default="true",
        help="return linear list of build dependencies",
    )
    group_graph_type.add_argument(
        "--graph",
        "-g",
        dest="linear",
        action="store_false",
        help="return dot graph of build dependencies",
    )
    args = parser.parse_args()

    if args.version:
        print("controlgraph {}".format(__version__))
        return 0

    # set up logging
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=10 * (3 - min(args.verbose, 2))
    )

    if not args.directories:
        args.directories = [p for p in Path.cwd().iterdir() if p.is_dir()]

    # Get graph and print
    dep_graph = graph(args.directories)
    if args.no_danglers:
        isolates = list(nx.isolates(dep_graph))
        dep_graph.remove_nodes_from(isolates)

    if args.linear:
        if args.danglers_first:
            # Put all isolated nodes first in list
            isolates = list(nx.isolates(dep_graph))
            dep_graph.remove_nodes_from(isolates)
            build_order = list(nx.dfs_postorder_nodes(dep_graph))
            print(" ".join(isolates + build_order))
        elif args.danglers_only:
            print(" ".join(list(nx.isolates(dep_graph))))
        else:
            print(" ".join(list(nx.dfs_postorder_nodes(dep_graph))))
    else:
        nx.nx_pydot.write_dot(dep_graph, sys.stdout)

    return 0


if __name__ == "__main__":
    sys.exit(main())
