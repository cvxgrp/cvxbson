import numpy as np
import pytest

from cvx.json import read_json, write_json


@pytest.mark.parametrize(
    "shape", [(50, 50), (1000, 50), (50, 1000), (1000, 1000), (5000, 2000)]
)
def test_read_and_write_json(tmp_path, shape):
    """
    Test that a numpy array is written and read correctly

    Args:
        tmp_path: temporary path fixture
        shape: shape of the matrix
    """
    data = {"a": np.random.rand(*shape), "b": 3.0, "c": "test"}
    write_json(tmp_path / "test.json", data)

    recovered_data = dict(read_json(tmp_path / "test.json"))

    assert data["b"] == recovered_data["b"]
    assert data["c"] == recovered_data["c"]

    # check numpy arrays are equal
    np.testing.assert_array_equal(data["a"], recovered_data["a"])
