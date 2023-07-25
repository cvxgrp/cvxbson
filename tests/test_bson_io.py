# -*- coding: utf-8 -*-
from __future__ import annotations

import pytest
import pandas as pd

from cvx.bson.file import build_bson


@pytest.fixture
def bson_file(resource_dir):
    file = resource_dir / "maffay.bson"
    return build_bson(file)


def test_prices(bson_file, prices):
    pd.testing.assert_frame_equal(
        bson_file.data["A"], prices
    )


def test_name(bson_file):
    assert bson_file.name == "maffay"


def test_parent(bson_file, resource_dir):
    assert bson_file.parent == resource_dir