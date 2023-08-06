"""Generate build order graph from directory of debian packaging repositories"""

__version__ = "0.1.0"

import argparse
import logging
import re
import sys

from pathlib import Path
from subprocess import run, PIPE, DEVNULL
from typing import Dict, List, Tuple

import dbp
import networkx as nx

L = logging.getLogger("dbp")
L.addHandler(logging.NullHandler())


def docker_capture_output(
    image: str, dist: str, cmd: List[str]
) -> Tuple[int, str, str]:
    """Returns exit code, stdout, and stderr"""
    rc = 0
    remove = True

    if dbp.container_exists():
        remove = False
    else:
        rc = dbp.docker_run(image, dist, "", dev=False)
        if rc != 0:
            L.error("Could not run container")
            return rc, "", "Could not run container"

    if not dbp.container_running(dist):
        rc = dbp.docker_start(dist)
        if rc != 0:
            L.error("Could not start stopped container")
            return rc, "", "Could not start stopped container"

    cmd = [
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

    L.debug("Running {}".format(" ".join(cmd)))
    proc = run(cmd, stdout=PIPE, stderr=PIPE)
    return proc.returncode, proc.stdout.decode("utf8"), proc.stderr.decode("utf8")


def get_source_map(dirs: List[Path]) -> Dict[str, str]:
    """Returns a map of binary packages to source packages found in `dirs`"""
    deps: Dict[str, str] = {}

    for p in dirs:
        control = Path(p / "debian/control").read_text()
        binaries: List[str] = []
        for line in control.split("\n"):
            if line.startswith("Package: "):
                deps[line[len("Package: ") :]] = p.stem

    return deps


def graph(dirs: List[Path]):
    valids: List[Path] = []
    for p in dirs:
        if Path(p / "debian/control").is_file():
            valids.append(p)
        else:
            L.warning("Directory {} is missing a debian/control file".format(p.stem))

    deps: Dict[str, List[str]] = {v.stem: [] for v in valids}
    deps_map = get_source_map(valids)
    for k, v in deps.items():
        rc, out, err = docker_capture_output(
            "opxhub/gbp",
            "stretch",
            ["dpkg-checkbuilddeps", "{}/debian/control".format(k)],
        )
        if rc == 1:
            versioned_deps = out.replace(
                "\x1b[1mdpkg-checkbuilddeps: \x1b[0m\x1b[1;31merror\x1b[0m: Unmet build dependencies:",
                "",
            ).strip()
            build_deps = re.sub(r" \([^\)]*\)", "", versioned_deps).split(" ")
            L.debug("Checking {} build deps {}".format(k, build_deps))
            for build_dep in build_deps:
                if build_dep in deps_map:
                    v.append(deps_map[build_dep])

    graph = nx.DiGraph()
    for k, v in deps.items():
        graph.add_node(k)
        graph.add_nodes_from(v)
        for dep in v:
            graph.add_edge(k, dep)

    print(" ".join(nx.dfs_postorder_nodes(graph)))


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

    L.debug("args: {}".format(args))

    graph(args.directories)

    return 0


if __name__ == "__main__":
    sys.exit(main())
