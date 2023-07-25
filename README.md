# [cvxjson](https://www.cvxgrp.org/cvxjson/)

[![PyPI version](https://badge.fury.io/py/cvxjson.svg)](https://badge.fury.io/py/cvxjson)
[![Apache 2.0 
License](https://img.shields.io/badge/License-APACHEv2-brightgreen.svg)](https://github.com/cvxgrp/cvxjson/blob/master/LICENSE)
[![PyPI download 
month](https://img.shields.io/pypi/dm/cvxjson.svg)](https://pypi.python.org/pypi/cvxjson/)
[![Coverage 
Status](https://coveralls.io/repos/github/cvxgrp/cvxjson/badge.png?branch=main)](https://coveralls.io/github/cvxgrp/cvxjson?branch=main)

[![Open in GitHub 
Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cvxgrp/cvxjson)

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
