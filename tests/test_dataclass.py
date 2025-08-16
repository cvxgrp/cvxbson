from dataclasses import dataclass

import numpy as np
import pandas as pd
import polars as pl

from cvx.bson.dataclass import Data


@dataclass(frozen=True)
class Maffay(Data):
    x: pd.DataFrame
    y: pl.DataFrame
    z: np.array


@dataclass(frozen=True)
class DataAPI(Data):
    # you need to explicitly declare the tables expected
    x: pd.DataFrame
    y: pl.DataFrame
    z: np.array

    def items(self):
        yield from self.__dict__.items()


def assert_equal(obj1, obj2):
    assert type(obj1) is type(obj2)

    if isinstance(obj1, pd.DataFrame):
        pd.testing.assert_frame_equal(obj1, obj2)

    if isinstance(obj1, np.ndarray):
        np.testing.assert_array_equal(obj1, obj2)

    if isinstance(obj1, pl.DataFrame):
        assert obj1.equals(obj2)


def test_conversion(tmp_path):
    matrix = np.random.rand(5, 2)

    x = pd.DataFrame(data=matrix)
    y = pl.DataFrame(data=2 * matrix)
    z = matrix

    data = Maffay(x=x, y=y, z=z)

    print(data.to_bson(file=tmp_path / "test.bson"))
    print(Maffay.from_bson(file=tmp_path / "test.bson"))


def test_reflection(tmp_path):
    matrix = np.random.rand(5, 2)

    x = pd.DataFrame(data=matrix)
    y = pl.DataFrame(data=2 * matrix)
    z = matrix

    data = {"x": x, "y": y, "z": z, "data": "xxx"}
    data = {key: value for key, value in data.items() if key in DataAPI.keys()}
    api = DataAPI(**data)

    for key, value in api.items():
        assert_equal(data[key], value)
