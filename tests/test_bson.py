# -*- coding: utf-8 -*-
from __future__ import annotations

import pandas as pd

from cvx.bson.io import read_bson
from cvx.bson.io import write_bson


def test_write(prices, tmp_path):
    dic = {"A": prices, "B": prices}
    write_bson(tmp_path / "maffay.bson", dic)
    assert (tmp_path / "maffay.bson").exists()

    x = dict(read_bson(tmp_path / "maffay.bson"))

    assert set(x.keys()) == {"A", "B"}
    pd.testing.assert_frame_equal(x["A"], prices)
    pd.testing.assert_frame_equal(x["B"], prices)

    # write_bson("maffay.bson", dic)