# -*- coding: utf-8 -*-
"""
Tools to support working with bson files
"""
from __future__ import annotations

from pathlib import Path

import pyarrow as pa
import simple_bson as bson


def read_bson(file: Path):
    """
    Read a bson file and prepare the bson_document needed

    Args:
        file:

    Returns:
        a bson-document
    """
    with open(file, mode="rb") as openfile:
        # Reading from bson file
        data = bson.loads(openfile.read())

        for name, value in data.items():
            yield name, pa.ipc.read_tensor(value).to_numpy()


def write_bson(file: Path, data):
    """
    Write dictionary into bson file

    Args:
        file: file
        dictionary of numpy arrays
    """

    def _encode_tensor(tensor: pa.lib.Tensor):
        try:
            sink = pa.BufferOutputStream()
            pa.ipc.write_tensor(tensor, sink)
            return sink.getvalue().to_pybytes()
        except Exception as e:
            print("Error encoding tensor:", str(e))
            return None

    content = bson.dumps(
        {
            name: _encode_tensor(pa.Tensor.from_numpy(matrix))
            for name, matrix in data.items()
        }
    )

    with open(file=file, mode="wb") as bson_file:
        bson_file.write(content)
