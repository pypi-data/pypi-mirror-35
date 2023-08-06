# controlgraph

[![PyPI version](https://badge.fury.io/py/controlgraph.svg)](https://pypi.org/project/controlgraph/)
[![Build status](https://badge.buildkite.com/81c4e486b5f9ff5d3bf3f3da820201cefad4965207f4e2a8c2.svg)](https://buildkite.com/opx/opx-infra-controlgraph)

Given a directory of repositories with Debian packaging, return the proper build order.

## Installation

```bash
pip3 install controlgraph
```

## Usage

With a bunch of directories present, run `controlgraph`.

```bash
$ git clone https://github.com/open-switch/SAI
$ git clone https://github.com/open-switch/opx-nas-acl
$ git clone https://github.com/open-switch/opx-nas-daemon
$ git clone https://github.com/open-switch/opx-logging
$ git clone https://github.com/open-switch/sai-bcm
$ git clone https://github.com/open-switch/opx-common-utils

$ controlgraph
opx-logging opx-common-utils opx-nas-acl opx-nas-daemon SAI opx-sai-bcm
```

Pair it with [`dbp`](https://github.com/opx-infra/dbp) for easy full builds.

```bash
$ dbp build $(controlgraph)

$ dbp shell
build@stretch:/mnt$ controlgraph
opx-logging SAI opx-nas-acl opx-sai-bcm opx-common-utils opx-nas-daemon
```
