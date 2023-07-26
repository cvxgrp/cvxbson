# -*- coding: utf-8 -*-
from __future__ import annotations

import io

import numpy as np
import pytest

from cvx.bson import read_bson, write_bson
from cvx.bson.file import to_bson, from_bson

@pytest.mark.parametrize("shape", [(50, 50), (1000, 50), (50, 1000), (1000, 1000)])
def test_write(tmp_path, shape):
    data = {"a": np.ones(shape)}
    write_bson(data=data, file=tmp_path / "maffay.bson")

    x = dict(read_bson(file=tmp_path / "maffay.bson"))

    assert set(x.keys()) == {"a"}
    np.allclose(x["a"], data["a"])


def test_wrong_type(tmp_path):
    data = {"B": 3}
    with pytest.raises(TypeError):
        write_bson(data=data, file=tmp_path / "maffay.bson")


def test_vector(tmp_path):
    data = {"a": np.array([1, 2, 3])}
    write_bson(data=data, file=tmp_path / "maffay.bson")

    x = dict(read_bson(file=tmp_path / "maffay.bson"))

    assert set(x.keys()) == {"a"}
    np.allclose(x["a"], data["a"])

@pytest.mark.parametrize("shape", [(50, 50), (1000, 50), (50, 1000), (1000, 1000), (5000,2000)])
def test_without_file(shape):
    data = {"a": np.ones(shape)}
    # Note that it takes already 40ms
    recovered = dict(from_bson(to_bson(data)))
    assert set(recovered.keys()) == {"a"}
    # it takes signifianctly longer with this test
    # assert np.allclose(aaa["a"], data["a"])


