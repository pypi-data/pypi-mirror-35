"""Generate build order graph from directory of debian packaging repositories"""

__version__ = "0.3.0"

import argparse
import logging
import re
import shutil
import sys

from pathlib import Path
from subprocess import Popen, run, PIPE, DEVNULL, STDOUT
from typing import Dict, List, Tuple

import dbp
import networkx as nx

L = logging.getLogger("dbp")
L.addHandler(logging.NullHandler())


def docker_exec_command(cmd: List[str]) -> List[str]:
    """Returns exit code, stdout, and stderr"""
    return [
        "docker",
        "exec",
        "-it",
        "--user=build",
        "-e=UID={}".format(dbp.UID),
        "-e=GID={}".format(dbp.GID),
        dbp.CONTAINER_NAME,
        "bash",
        "-l",
        "-c",
        " ".join(cmd),
    ]


def get_source_map(dirs: List[Path]) -> Dict[str, str]:
    """Returns a map of binary packages to source packages found in `dirs`"""
    deps = {}

    for p in dirs:
        control = Path(p / "debian/control").read_text()
        binaries = []
        for line in control.split("\n"):
            if line.startswith("Package: "):
                deps[line[len("Package: ") :]] = p.stem

    return deps


def graph(dirs: List[Path], linear=True):
    """Prints linear build order. If dpkg-checkbuilddeps is not available, a container
    started with dbp.docker_run must be already running.
    """
    valids = []
    for p in dirs:
        if Path(p / "debian/control").is_file():
            valids.append(p)
        else:
            L.info("Directory {} is missing a debian/control file".format(p.stem))

    deps = {v.stem: [] for v in valids}

    # time to collect all unmet build dependencies in parallel
    commands = {}
    for k, v in deps.items():
        if shutil.which("dpkg-checkbuilddeps") is None:
            commands[k] = docker_exec_command(
                ["dpkg-checkbuilddeps", "{}/debian/control".format(k)]
            )
        else:
            commands[k] = ["dpkg-checkbuilddeps", "{}/debian/control".format(k)]

    processes = {
        repo: Popen(cmd, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
        for repo, cmd in commands.items()
    }

    deps_map = get_source_map(valids)

    for repo, proc in processes.items():
        proc.wait()
        # process returned build dependencies
        if proc.returncode == 1:
            for line in proc.stdout:
                versioned_deps = line.replace(
                    "dpkg-checkbuilddeps: error: Unmet build dependencies:", ""
                ).strip()
                build_deps = re.sub(r" \([^\)]*\)", "", versioned_deps).split(" ")
                L.debug("Checking {} build deps {}".format(repo, build_deps))
                for build_dep in build_deps:
                    if build_dep in deps_map:
                        deps[repo].append(deps_map[build_dep])

    graph = nx.DiGraph()
    for k, v in deps.items():
        graph.add_node(k)
        graph.add_nodes_from(v)
        for dep in v:
            graph.add_edge(k, dep)

    if linear:
        print(" ".join(nx.dfs_postorder_nodes(graph)))
    else:
        nx.nx_pydot.write_dot(graph, sys.stdout)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version", "-V", action="store_true", help="print program version"
    )
    parser.add_argument(
        "--verbose", "-v", help="-v for info, -vv for debug", action="count", default=0
    )
    parser.add_argument(
        "--rm", action="store_true", help="remove container when finished"
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

    if shutil.which("dpkg-checkbuilddeps") is None:
        # Using Docker, time to start container
        if not dbp.container_exists():
            rc = dbp.docker_run("opxhub/gbp", "stretch", "", dev=False)
            if rc != 0:
                L.error("Could not run container")
                return rc

        if not dbp.container_running("stretch"):
            rc = dbp.docker_start("stretch")
            if rc != 0:
                L.error("Could not start stopped container")
                return rc

    graph(args.directories, args.linear)

    if args.rm:
        dbp.remove_container()

    return 0


if __name__ == "__main__":
    sys.exit(main())
