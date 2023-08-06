# controlgraph

[![PyPI version](https://badge.fury.io/py/controlgraph.svg)](https://pypi.org/project/controlgraph/)
[![Build status](https://badge.buildkite.com/81c4e486b5f9ff5d3bf3f3da820201cefad4965207f4e2a8c2.svg)](https://buildkite.com/opx/opx-infra-controlgraph)

controlgraph is a directed graph which can be traversed to enable parallelized Debian package builds.

From the available directories with valid Debian packaging, a graph with directories (representing source packages) for nodes and build dependencies for edges is produced. This can traversed with a depth-first search to build in dependency order.

`controlgraph` is a program which returns the controlgraph for a directory to build, in linear or dot format.

## Installation

```bash
pip3 install controlgraph
```

## Usage

With one or more directories present, run `controlgraph`.

```bash
$ for r in opx-nas-acl opx-nas-daemon opx-alarm opx-logging opx-common-utils; do
    git clone "https://github.com/open-switch/$r"
  done

$ controlgraph
opx-alarm opx-logging opx-common-utils opx-nas-acl opx-nas-daemon

$ controlgraph --graph
strict digraph  {
"opx-alarm";
"opx-nas-daemon";
"opx-common-utils";
"opx-logging";
"opx-nas-acl";
"opx-nas-daemon" -> "opx-common-utils";
"opx-nas-daemon" -> "opx-logging";
"opx-nas-daemon" -> "opx-nas-acl";
"opx-common-utils" -> "opx-logging";
"opx-nas-acl" -> "opx-common-utils";
"opx-nas-acl" -> "opx-logging";
}
```

Pair it with [`dbp`](https://github.com/opx-infra/dbp) for easy full builds.

```bash
$ dbp build $(controlgraph)
```
