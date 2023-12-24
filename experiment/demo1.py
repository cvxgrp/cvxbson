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
    data = DataAPI(A=pl.DataFrame(), B=pl.DataFrame(), C=pl.DataFrame())
    print(data.tables)
    print(data.A)
    print(data.B)
    print(data.C)
