# -*- coding: utf-8 -*-
"""
Tools to support working with json files
"""
import json
from collections.abc import Iterable
from os import PathLike
from typing import Any, Dict

import numpy as np
from numpyencoder import NumpyEncoder


def read_json(
    json_file: str | bytes | PathLike[str] | PathLike[bytes] | int,
) -> Dict[str, Any]:
    """Read a json file and return a genaerator of key-value pairs"""
    with open(json_file, "r") as f:
        json_data = json.load(f)
        d = {}
        for name, data in json_data.items():
            if isinstance(data, Iterable):
                d[name] = np.asarray(data)
            else:
                d[name] = data

        return d


def write_json(
    json_file: str | bytes | PathLike[str] | PathLike[bytes] | int, data: Dict[str, Any]
) -> None:
    """Write a json file with the data"""
    with open(json_file, "w") as f:
        json.dump(data, f, cls=NumpyEncoder)
