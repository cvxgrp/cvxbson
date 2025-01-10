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
"""
Tools to support working with bson files and strings
"""

from __future__ import annotations

from os import PathLike
from typing import Any, Dict, Union

import bson
import numpy.typing as npt
import pandas as pd

# see https://github.com/microsoft/pylance-release/issues/2019
from typing_extensions import TypeAlias

from .io import decode, encode

FILE = Union[str, bytes, PathLike]
MATRIX: TypeAlias = Union[npt.NDArray[Any], pd.DataFrame]
MATRICES = Dict[str, MATRIX]


def read_bson(file: FILE) -> MATRICES:
    """
    Read a bson file and prepare the bson_document needed

    Args:
        file:

    Returns:
        A dictionary of numpy arrays


    """
    with open(file, mode="rb") as openfile:
        # Reading from bson file
        return from_bson(bson_str=openfile.read())


def write_bson(file: FILE, data: MATRICES) -> int:
    """
    Write dictionary into a bson file

    Args:
        file: file
        data: dictionary of numpy arrays
    """
    with open(file=file, mode="wb") as bson_file:
        return bson_file.write(to_bson(data=data))


def to_bson(data: MATRICES) -> bytes:
    """
    Convert a dictionary of numpy arrays into a bson string

    Args:
        data: dictionary of numpy arrays
    """
    return bytes(bson.dumps({name: encode(matrix) for name, matrix in data.items()}))


def from_bson(bson_str: bytes) -> MATRICES:
    """Convert a bson string into a dictionary of numpy arrays"""
    return {name: decode(value) for name, value in bson.loads(bson_str).items()}
