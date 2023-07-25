# -*- coding: utf-8 -*-
"""
Tools to support working with bson files
"""
from __future__ import annotations

import io
from pathlib import Path

import numpy as np
import simple_bson as bson
import pyarrow as pa
import pyarrow.parquet as pq

def read_bson(file: Path):
    """
    Read a bson file and prepare the bson_document needed

    Args:
        file:

    Returns:
        a bson-document
    """
    assert file.exists()

    with open(file, mode="rb") as openfile:
        # Reading from bson file
        bson_document = openfile.read()
        data = bson.loads(bson_document)

        for name, value in data.items():
            xxx = np.array([row for row in pq.read_table(io.BytesIO(value))])
            yield name, xxx



def write_bson(file: Path, dic, compression="zstd"):
    """
    Write dictionary into bson file

    Args:
        file: file
        dictionary of polars dataframes
        logger: logger

    """

    def to_binary(matrix: np.ndarray):
        """
        byte-stream of a frame

        Args:
            matrix: the frame converted to ipc

        Returns:
            the bytestream
        """

        with io.BytesIO() as buffer:
            if isinstance(matrix, np.ndarray):

                arrays = [
                    pa.array(col)  # Create one arrow array per row
                    for col in matrix
                ]

                table = pa.Table.from_arrays(
                    arrays,
                    names=[str(i) for i in range(np.shape(arrays)[0])]
                    # give name to each row
                )

                pq.write_table(table, buffer, compression=compression)

            else:
                raise ValueError("Bson only supports numpy arrays")

            return buffer.getvalue()

    content = bson.dumps({name: to_binary(value) for name, value in dic.items()})

    with open(file=file, mode="wb") as bson_file:
        bson_file.write(content)

    return file
