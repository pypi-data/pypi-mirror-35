# controlgraph

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
dbp build $(controlgraph)
```
