# [cvxbson](https://www.cvxgrp.org/cvxbson/)

[![PyPI version](https://badge.fury.io/py/cvxbson.svg)](https://badge.fury.io/py/cvxbson)
[![Apache 2.0
License](https://img.shields.io/badge/License-APACHEv2-brightgreen.svg)](https://github.com/cvxgrp/cvxbson/blob/master/LICENSE)
[![PyPI download
month](https://img.shields.io/pypi/dm/cvxbson.svg)](https://pypi.python.org/pypi/cvxbson/)
[![Coverage
Status](https://coveralls.io/repos/github/cvxgrp/cvxbson/badge.png?branch=main)](https://coveralls.io/github/cvxgrp/cvxbson?branch=main)

## Poetry

We assume you share already the love for [Poetry](https://python-poetry.org).
Once you have installed poetry you can perform

```bash
poetry install
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
