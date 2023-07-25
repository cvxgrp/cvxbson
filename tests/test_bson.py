# -*- coding: utf-8 -*-
from __future__ import annotations

import numpy as np
import pytest

from cvx.bson import read_bson, write_bson


@pytest.mark.parametrize("shape", [(50, 50), (1000, 50), (50, 1000), (1000, 1000)])
def test_write(tmp_path, shape):
    data = {"a": np.random.rand(*shape)}
    write_bson(tmp_path / "maffay.bson", data)

    x = dict(read_bson(tmp_path / "maffay.bson"))

    assert set(x.keys()) == {"a"}
    np.allclose(x["a"], data["a"])


def test_wrong_type(tmp_path):
    dic = {"B": 3}
    with pytest.raises(TypeError):
        write_bson(tmp_path / "maffay.bson", dic)


def test_vector(tmp_path):
    dic = {"a": np.array([1, 2, 3])}
    write_bson(tmp_path / "maffay.bson", dic)

    x = dict(read_bson(tmp_path / "maffay.bson"))

    assert set(x.keys()) == {"a"}
    np.allclose(x["a"], dic["a"])
