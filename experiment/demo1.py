from dataclasses import dataclass, field
from typing import Dict

import polars as pl

from cvx.bson.dataclass import Data


@dataclass(frozen=True)
class DataAPI(Data):
    # List of tables expected
    A: pl.DataFrame
    B: pl.DataFrame
    C: pl.DataFrame

    # Define a mutable value for the mapping from short name to full name
    tables: Dict[str, str] = field(
        default_factory=lambda: {"A": "AAA", "B": "BBB", "C": "CCC"}
    )


if __name__ == "__main__":
    # We add this as a little demo
    import numpy as np

    data = DataAPI(
        A=pl.DataFrame(np.random.rand(10, 5)),
        B=pl.DataFrame(np.random.rand(20, 3)),
        C=pl.DataFrame(np.random.rand(50, 5)),
    )

    # We can access the tables
    print(data.tables)
    print(data.A)
    print(data.B)
    print(data.C)

    # convert all data into one bson file
    print(data.to_bson("xxx.bson"))

    data2 = DataAPI.from_bson("xxx.bson")
    print(data2)

    def strategy(api: DataAPI):
        # the strategy has no idea how the data is stored
        print(api.A)

    strategy(data2)
