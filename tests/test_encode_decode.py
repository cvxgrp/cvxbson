"""Tests for encoding and decoding different data types.

This module tests the encode and decode functions for different data types
including Polars DataFrames, Pandas DataFrames, and NumPy arrays.
"""

import numpy as np
import pandas as pd
import polars as pl

from cvx.bson.io import decode, encode


def test_pl():
    """Test encoding and decoding of Polars DataFrames.

    This test creates a Polars DataFrame, encodes it, decodes it,
    and verifies that the original and decoded DataFrames are equal.
    """
    frame = pl.DataFrame(data=np.random.rand(10, 5))
    b = decode(encode(frame))
    assert frame.equals(b)


def test_pd():
    """Test encoding and decoding of Pandas DataFrames.

    This test creates a Pandas DataFrame, encodes it, decodes it,
    and verifies that the original and decoded DataFrames are equal.
    """
    frame = pd.DataFrame(data=np.random.rand(10, 5))
    b = decode(encode(frame))
    pd.testing.assert_frame_equal(b, frame)


def test_np():
    """Test encoding and decoding of NumPy arrays.

    This test creates a NumPy array, encodes it, decodes it,
    and verifies that the original and decoded arrays are equal.
    """
    matrix = np.random.rand(10, 5)
    b = decode(encode(matrix))
    np.testing.assert_array_equal(matrix, b)
