"""Tests for dataclass serialization and deserialization with BSON.

This module tests the functionality of the Data base class for dataclasses,
including serialization to BSON, deserialization from BSON, and data access patterns.
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd
import polars as pl

from cvx.bson.dataclass import Data


@dataclass(frozen=True)
class Maffay(Data):
    """Test dataclass for BSON serialization.

    This class demonstrates a dataclass that can be serialized to and from BSON.
    """

    x: pd.DataFrame
    y: pl.DataFrame
    z: np.array


@dataclass(frozen=True)
class DataAPI(Data):
    """Test data API class for BSON serialization.

    This class demonstrates a dataclass with custom methods that can be
    serialized to and from BSON.
    """

    # you need to explicitly declare the tables expected
    x: pd.DataFrame
    y: pl.DataFrame
    z: np.array

    def items(self):
        """Get the field names and values of this dataclass instance.

        Yields:
            Pairs of (field_name, field_value)
        """
        yield from self.__dict__.items()


def assert_equal(obj1, obj2):
    """Assert that two objects are equal, handling different data types.

    This function compares different types of objects (pandas DataFrames,
    numpy arrays, polars DataFrames) using the appropriate equality check.

    Args:
        obj1: First object to compare
        obj2: Second object to compare
    """
    assert type(obj1) is type(obj2)

    if isinstance(obj1, pd.DataFrame):
        pd.testing.assert_frame_equal(obj1, obj2)

    if isinstance(obj1, np.ndarray):
        np.testing.assert_array_equal(obj1, obj2)

    if isinstance(obj1, pl.DataFrame):
        assert obj1.equals(obj2)


def test_conversion(tmp_path):
    """Test conversion of a dataclass to and from BSON.

    This test creates a dataclass instance, serializes it to BSON,
    and then deserializes it back.

    Args:
        tmp_path: Temporary path fixture
    """
    matrix = np.random.rand(5, 2)

    x = pd.DataFrame(data=matrix)
    y = pl.DataFrame(data=2 * matrix)
    z = matrix

    data = Maffay(x=x, y=y, z=z)

    print(data.to_bson(file=tmp_path / "test.bson"))
    print(Maffay.from_bson(file=tmp_path / "test.bson"))


def test_reflection(tmp_path):
    """Test reflection of data through a dataclass.

    This test creates a dictionary of data, filters it based on the
    dataclass fields, creates a dataclass instance, and then verifies
    that the data is preserved.

    Args:
        tmp_path: Temporary path fixture
    """
    matrix = np.random.rand(5, 2)

    x = pd.DataFrame(data=matrix)
    y = pl.DataFrame(data=2 * matrix)
    z = matrix

    data = {"x": x, "y": y, "z": z, "data": "xxx"}
    data = {key: value for key, value in data.items() if key in DataAPI.keys()}
    api = DataAPI(**data)

    for key, value in api.items():
        assert_equal(data[key], value)
