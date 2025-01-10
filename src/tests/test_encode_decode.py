import numpy as np
import pandas as pd
import polars as pl

from cvx.bson.io import decode, encode


def test_pl():
    frame = pl.DataFrame(data=np.random.rand(10, 5))
    b = decode(encode(frame))
    assert frame.equals(b)


def test_pd():
    frame = pd.DataFrame(data=np.random.rand(10, 5))
    b = decode(encode(frame))
    pd.testing.assert_frame_equal(b, frame)


def test_np():
    matrix = np.random.rand(10, 5)
    b = decode(encode(matrix))
    np.testing.assert_array_equal(matrix, b)
