"""Generate build order graph from directory of debian packaging repositories"""

__version__ = "0.4.0"

import argparse
import logging
import re
import sys

from pathlib import Path
from subprocess import Popen, run, PIPE, DEVNULL, STDOUT
from typing import Dict, List, Tuple

import networkx as nx

from debian import deb822

L = logging.getLogger("controlgraph")
L.addHandler(logging.NullHandler())


class BinaryPackage:
    def __init__(self, name: str, source: str, build_deps: List[str]) -> None:
        self.name = name
        self.source = source
        self.build_deps = build_deps

    def __repr__(self) -> str:
        return "BinaryPackage({})".format(self.__dict__)


def parse_controlfile(path: Path) -> Dict[str, BinaryPackage]:
    source = ""
    build_deps = []
    pkgs = {}
    with path.open() as f:
        for src in deb822.Sources.iter_paragraphs(f):
            if "Source" in src:
                source = src["Source"]
                build_deps.extend(
                    [
                        re.sub(r" \([^\)]*\)", "", s.strip()).strip()
                        for s in src["Build-Depends"].split(",")
                    ]
                )
            elif "Package" in src:
                pkgs[src["Package"]] = BinaryPackage(src["Package"], source, build_deps)
    return pkgs


def graph(dirs: List[Path]) -> nx.DiGraph:
    """Prints linear or dot graph build order."""
    # Get dict matching binary packages to source packages/build deps
    pkgs = {}
    for p in dirs:
        controlfile = Path(p / "debian/control")
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
    graph = nx.DiGraph()
    for k, v in build_deps.items():
        graph.add_node(k)
        graph.add_nodes_from(v)
        for dep in v:
            graph.add_edge(k, dep)

    return graph


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version", "-V", action="store_true", help="print program version"
    )
    parser.add_argument(
        "--verbose", "-v", help="-v for info, -vv for debug", action="count", default=0
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

    if len(args.directories) == 0:
        args.directories = [p for p in Path.cwd().iterdir() if p.is_dir()]

    # Get graph and print
    g = graph(args.directories)
    if args.linear:
        # Put all isolated nodes first in list
        isolates = list(nx.isolates(g))
        g.remove_nodes_from(isolates)
        build_order = list(nx.dfs_postorder_nodes(g))
        print(" ".join(isolates + build_order))
    else:
        nx.nx_pydot.write_dot(g, sys.stdout)

    return 0


if __name__ == "__main__":
    sys.exit(main())
