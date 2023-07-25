# -*- coding: utf-8 -*-
from __future__ import annotations

import numpy as np
import pytest

from cvx.bson.file import build_bson
from cvx.bson.io import write_bson


@pytest.fixture()
def random_matrix():
    np.random.seed(2)
    return np.random.rand(5,3)


@pytest.fixture()
def bson_file(tmp_path, random_matrix):
    file = tmp_path / "maffay.bson"
    write_bson(file, {"random": random_matrix})
    return build_bson(file)


def test_prices(bson_file, random_matrix):
    assert np.allclose(
        bson_file.data["random"], random_matrix
    )


def test_name(bson_file):
    assert bson_file.name == "maffay"


def test_parent(bson_file, tmp_path):
    assert bson_file.parent == tmp_path