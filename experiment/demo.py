"""Demonstration of using dataclasses with BSON serialization.

This module shows how to create a dataclass that can be serialized to and from BSON,
and how to use it in a strategy pattern.
"""

from dataclasses import dataclass, field

import polars as pl

from cvx.bson.dataclass import Data


@dataclass(frozen=True)
class DataAPI(Data):
    """Data API class that holds multiple Polars DataFrames.

    This class demonstrates how to create a dataclass that inherits from Data
    to enable BSON serialization and deserialization.
    """

    # List of tables expected
    A: pl.DataFrame
    B: pl.DataFrame
    C: pl.DataFrame

    # Define a mutable value for the mapping from short name to full name
    tables: dict[str, str] = field(default_factory=lambda: {"A": "AAA", "B": "BBB", "C": "CCC"})


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
    print(data.to_bson("data.bson"))

    data2 = DataAPI.from_bson("data.bson")
    print(data2)

    def strategy(api: DataAPI):
        """Process data using the DataAPI.

        This function demonstrates the strategy pattern where the function
        receives a data API and doesn't need to know how the data is stored.

        Args:
            api: The data API containing the required data
        """
        # the strategy has no idea how the data is stored
        print(api.A)

    strategy(data2)
