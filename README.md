# 📦 [cvxbson](https://www.cvxgrp.org/cvxbson/book)

[![PyPI version](https://badge.fury.io/py/cvxbson.svg)](https://badge.fury.io/py/cvxbson)
[![Apache 2.0
License](https://img.shields.io/badge/License-APACHEv2-brightgreen.svg)](https://github.com/cvxgrp/cvxbson/blob/master/LICENSE)
[![Downloads](https://static.pepy.tech/personalized-badge/cvxbson?period=month&units=international_system&left_color=black&right_color=orange&left_text=PyPI%20downloads%20per%20month)](https://pepy.tech/project/cvxbson)
[![Coverage Status](https://coveralls.io/repos/github/cvxgrp/cvxbson/badge.png?branch=main)](https://coveralls.io/github/cvxgrp/cvxbson?branch=main)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://github.com/renovatebot/renovate)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cvxgrp/cvxbson)

## 🔄 IPC

IPC stands for InterProcess Communication. It is a mechanism that allows to share
data between processes. A traditional way to do so is to use json files.
Json files are rather flexible and can be used to share data between different
programming languages. However, they are not very efficient.

Here we use their binary counterpart, bson files. Bson files are much more efficient
but somewhat lack the flexibility of json files. Here we rely on the [bson](https://pypi.org/project/bson/)
package to read and write bson files. We are interested in parsing dictionaries
of numpy arrays, pandas and  polars dataframes as fast as possible.

There might be faster ways to achieve this goal and we are open to suggestions
and pull requests.

We recommend using json files to transfer configurations and small amounts of data.
Bson files can then be used to transfer large matrices. A coexistence is possible
and encouraged.

## 🚀 Demo

```python
>>> import numpy as np

>>> from src.cvx.bson import read_bson, write_bson

>>> data = {"A": np.random.rand(50, 50), "B": np.random.rand(50)}

>>> write_bson("test.bson", data)
>>> recovered = read_bson("test.bson")

>>> assert np.allclose(data["A"], recovered["A"])
>>> assert np.allclose(data["B"], recovered["B"])
```

We have also implemented the same functionality in for json files but would advise
against using it. It is much slower and less efficient.

You may want to avoid the explicit construction of files.
It is possible to work directly with bson strings. We provide methods for that, too.

## 🛠️ uv

You need to install [task](https://taskfile.dev).
Starting with

```bash
task build:install
```

will install [uv](https://github.com/astral-sh/uv) and create
the virtual environment defined in
pyproject.toml and locked in uv.lock.

## 📊 marimo

We install [marimo](https://marimo.io) on the fly within the aforementioned
virtual environment. Executing

```bash
task docs:marimo
```

will install and start marimo.
