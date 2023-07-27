# [cvxbson](https://www.cvxgrp.org/cvxbson/)

[![PyPI version](https://badge.fury.io/py/cvxbson.svg)](https://badge.fury.io/py/cvxbson)
[![Apache 2.0
License](https://img.shields.io/badge/License-APACHEv2-brightgreen.svg)](https://github.com/cvxgrp/cvxbson/blob/master/LICENSE)
[![PyPI download
month](https://img.shields.io/pypi/dm/cvxbson.svg)](https://pypi.python.org/pypi/cvxbson/)
[![Coverage
Status](https://coveralls.io/repos/github/cvxgrp/cvxbson/badge.png?branch=main)](https://coveralls.io/github/cvxgrp/cvxbson?branch=main)

## IPC

IPC stands for InterProcess Communication. It is a mechanism that allows to share
data between processes. A traditional way to do so is to use json files.
Json files are rather flexible and can be used to share data between different
programming languages. However, they are not very efficient.

Here we use their binary counterpart, bson files. Bson files are much more efficient
but somewhat lack the flexibility of json files. Here we rely on the [bson](https://pypi.org/project/bson/)
package to read and write bson files. We are interested in parsing dictionaries
of numpy arrays as fast as possible. Our current implementation is converting
numpy arrays to pyarrow tensors and then to bson.

There might be faster ways to achieve this goal and we are open to suggestions
and pull requests.

We recommend using json files to transfer configurations and small amounts of data.
Bson files can then be used to transfer large matrices. A coexistence is possible
and encouraged.

## Demo

```python
import numpy as np

from cvx.bson import read_bson, write_bson

data = {"A": np.random.rand(50,50), "B": np.random.rand(50)}

write_bson("test.bson", data)
recovered = read_bson("test.bson")

assert np.allclose(data["A"], recovered["A"])
assert np.allclose(data["B"], recovered["B"])
```

We have also implemented the same functionality in for json files but would advise
against using it. It is much slower and less efficient.

You may want to avoid the explicit construction of files.
It is possible to work directly with bson strings. We provide methods for that, too.

## Poetry

We assume you share already the love for [Poetry](https://python-poetry.org).
Once you have installed poetry you can perform

```bash
make install
```

to replicate the virtual environment we have defined in pyproject.toml.

## Kernel

We install [JupyterLab](https://jupyter.org) within your new virtual
environment. Executing

```bash
make kernel
```

constructs a dedicated [Kernel](https://docs.jupyter.org/en/latest/projects/kernels.html)
for the project.
