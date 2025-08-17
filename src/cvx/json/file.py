#    Copyright 2023 Stanford University Convex Optimization Group
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""Tools to support working with json files."""

import json
from collections.abc import Iterable
from os import PathLike
from typing import Any

import numpy as np
import numpy.typing as npt

from .numpyencoder import NumpyEncoder

FILE = str | bytes | PathLike
MATRIX = npt.NDArray[Any]
DATA = dict[str, Any]


def read_json(json_file: FILE) -> DATA:
    """Read a JSON file and convert its contents to a dictionary.

    Iterables in the JSON data are converted to numpy arrays.

    Args:
        json_file: Path to the JSON file to read

    Returns:
        A dictionary containing the data from the JSON file
    """
    with open(json_file) as f:
        json_data = json.load(f)
        d = {}
        for name, data in json_data.items():
            if isinstance(data, Iterable):
                d[name] = np.asarray(data)
            else:
                d[name] = data

        return d


def write_json(json_file: FILE, data: DATA) -> None:
    """Write data to a JSON file.

    Uses NumpyEncoder to handle numpy data types.

    Args:
        json_file: Path to the JSON file to write
        data: Dictionary of data to write to the file
    """
    with open(json_file, "w") as f:
        json.dump(data, f, cls=NumpyEncoder)
