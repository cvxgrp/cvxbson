# -*- coding: utf-8 -*-
from __future__ import annotations

import numpy as np
import pytest

from cvx.bson.file import read_bson
from cvx.bson.file import write_bson


@pytest.fixture()
def random_matrix():
    np.random.seed(2)
    return np.random.rand(5,3)


def test_write(random_matrix, tmp_path):
    dic = {"B": random_matrix}
    write_bson(tmp_path / "maffay.bson", dic)
    assert (tmp_path / "maffay.bson").exists()

    x = dict(read_bson(tmp_path / "maffay.bson"))

    assert set(x.keys()) == {"B"}
    np.allclose(x["B"], random_matrix)
