import numpy as np
import pandas as pd
import polars as pl
import pytest

from cvx.bson.file import from_bson, to_bson


@pytest.fixture()
def data():
    return {
        "frame": pd.DataFrame(data=np.random.rand(5, 2)),
        "numpy": np.random.rand(5, 2),
        "frame_with_time": pd.DataFrame(
            data=np.random.rand(2, 2),
            index=[pd.Timestamp("2020-01-01"), pd.Timestamp("2022-01-01")],
        ),
        "polars": pl.DataFrame(data=np.random.rand(10, 3)),
    }


def assert_equal(obj1, obj2):
    assert type(obj1) is type(obj2)

    if isinstance(obj1, pd.DataFrame):
        pd.testing.assert_frame_equal(obj1, obj2)

    if isinstance(obj1, np.ndarray):
        np.testing.assert_array_equal(obj1, obj2)

    if isinstance(obj1, pl.DataFrame):
        assert obj1.equals(obj2)


def test_roundtrip(data):
    """Testing the roundtrip.

    Args:
        data: Fixture exposing a dictionary of data
    """
    reproduced = from_bson(to_bson(data))
    for key, value in reproduced.items():
        assert_equal(value, data[key])


def test_file(data, tmp_path):
    with open(file=tmp_path / "xxx.bson", mode="wb") as bson_file:
        bson_file.write(to_bson(data))

    with open(file=tmp_path / "xxx.bson", mode="rb") as bson_file:
        reproduced = from_bson(bson_file.read())

    for key, value in reproduced.items():
        assert_equal(reproduced[key], data[key])
