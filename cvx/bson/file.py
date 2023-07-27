# -*- coding: utf-8 -*-
"""
Tools to support working with bson files and strings
"""
from __future__ import annotations

from os import PathLike
from typing import Dict

import numpy as np
import pyarrow as pa  # type: ignore

import bson  # type: ignore


def read_bson(
    file: str | bytes | PathLike[str] | PathLike[bytes] | int,
) -> Dict[str, np.ndarray]:
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


def write_bson(
    file: str | bytes | PathLike[str] | PathLike[bytes] | int,
    data: Dict[str, np.ndarray],
) -> int:
    """
    Write dictionary into a bson file

    Args:
        file: file
        data: dictionary of numpy arrays
    """
    bson_str = to_bson(data=data)
    with open(file=file, mode="wb") as bson_file:
        return bson_file.write(bson_str)


def to_bson(data: Dict[str, np.ndarray]) -> bytes:
    """
    Convert a dictionary of numpy arrays into a bson string

    Args:
        data: dictionary of numpy arrays
    """

    def _encode_tensor(tensor: pa.lib.Tensor):
        buffer = pa.BufferOutputStream()
        pa.ipc.write_tensor(tensor, buffer)
        return buffer.getvalue().to_pybytes()

    return bson.dumps(
        {
            name: _encode_tensor(pa.Tensor.from_numpy(obj=matrix))
            for name, matrix in data.items()
        }
    )


def from_bson(bson_str: bytes) -> Dict[str, np.ndarray]:
    """Convert a bson string into a dictionary of numpy arrays"""
    data = bson.loads(bson_str)

    # for name, value in data.items():
    return {name: pa.ipc.read_tensor(value).to_numpy() for name, value in data.items()}
