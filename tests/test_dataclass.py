from dataclasses import dataclass

import numpy as np
import pandas as pd
import polars as pl

from cvx.bson.dataclass import Data


@dataclass(frozen=True)
class Maffay(Data):
    x: pd.DataFrame
    y: pl.DataFrame
    z: np.array


def test_conversion(tmp_path):
    matrix = np.random.rand(5, 2)

    x = pd.DataFrame(data=matrix)
    y = pl.DataFrame(data=2 * matrix)
    z = matrix

    data = Maffay(x=x, y=y, z=z)

    print(data.to_bson(file=tmp_path / "test.bson"))

    print(Maffay.from_bson(file=tmp_path / "test.bson"))
