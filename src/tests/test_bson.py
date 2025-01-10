from __future__ import annotations

import numpy as np
import pytest

from src.cvx.bson.file import from_bson, read_bson, to_bson, write_bson


@pytest.mark.parametrize("shape", [(50, 50), (1000, 50), (50, 1000), (1000, 1000), (5000, 2000)])
def test_write(tmp_path, shape):
    """
    Test that a numpy array is written and read correctly

    Args:
        tmp_path: temporary path fixture
        shape: shape of the matrix
    """
    data = {"a": np.ones(shape)}
    write_bson(data=data, file=tmp_path / "maffay.bson")

    x = read_bson(file=tmp_path / "maffay.bson")

    assert set(x.keys()) == {"a"}
    np.allclose(x["a"], data["a"])


def test_vector(tmp_path):
    """
    Test that a vector is written and read correctly

    Args:
        tmp_path: temporary path fixture
    """
    data = {"a": np.array([1, 2, 3])}
    write_bson(data=data, file=tmp_path / "maffay.bson")

    x = read_bson(file=tmp_path / "maffay.bson")

    assert set(x.keys()) == {"a"}
    np.allclose(x["a"], data["a"])


@pytest.mark.parametrize("shape", [(50, 50), (1000, 50), (50, 1000), (1000, 1000), (5000, 2000)])
def test_without_file(shape):
    """
    Test that a matrix is written and read correctly

    Args:
        shape: shape of the matrix
    """
    data = {"a": np.ones(shape)}
    # Note that it takes already 40ms
    recovered = from_bson(to_bson(data))
    assert set(recovered.keys()) == {"a"}
    # it takes signifianctly longer with this line
    assert np.allclose(recovered["a"], data["a"])
