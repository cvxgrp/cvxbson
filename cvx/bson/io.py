# -*- coding: utf-8 -*-
"""
Tools to support working with bson files
"""
from __future__ import annotations

import io
from pathlib import Path

import pandas as pd
import simple_bson as bson


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
            yield name, pd.read_parquet(io.BytesIO(value))


def write_bson(file: Path, dic, compression="zstd"):
    """
    Write dictionary into bson file

    Args:
        file: file
        dictionary of polars dataframes
        logger: logger

    """

    def to_binary(frame):
        """
        ipc byte-stream of a frame

        Args:
            frame: the frame converted to ipc

        Returns:
            the bytestream
        """

        with io.BytesIO() as buffer:
            frame.to_parquet(buffer, compression=compression)
            return buffer.getvalue()

    content = bson.dumps({name: to_binary(value) for name, value in dic.items()})

    with open(file=file, mode="wb") as bson_file:
        bson_file.write(content)

    return file