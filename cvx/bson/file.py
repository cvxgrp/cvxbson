# -*- coding: utf-8 -*-
"""
Dataclass to simplify dealing with bson files.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict

from .io import read_bson


def build_bson(file):
    """
    Construct the frozen Dataclass for a BsonFile with this builder.

    Args:
        file: Path to *.bson file.

    Returns:
        _BsonFile object.
    """
    return _BsonFile(file, dict(read_bson(file)))


@dataclass(frozen=True)
class _BsonFile:
    """
    A BsonFile contains the keys meta, tables and timeseries.

    Attributes:
        file: Path to *.bson file.
        data: Dict with data stored in a file.
    """

    file: Path
    data: Dict = None

    @property
    def name(self):
        """
        Name of the file.
        """
        return self.file.stem

    @property
    def parent(self):
        """
        Parent of the file (e.g. path).
        """
        return self.file.parent