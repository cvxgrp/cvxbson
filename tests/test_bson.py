# -*- coding: utf-8 -*-
from __future__ import annotations

import numpy as np
import pytest

from cvx.bson.io import read_bson
from cvx.bson.io import write_bson


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

    #write_bson("maffay.bson", dic)


# def test():
#     import numpy as np
#     import pyarrow as pa
#     import pyarrow.parquet as pq
#
#     matrix = np.random.rand(5, 3)
#     arrays = [
#         pa.array(row)  # Create one arrow array per row
#         for row in matrix
#     ]
#     print(arrays)
#     #assert False
#
#     table = pa.Table.from_arrays(
#         arrays,
#         names=[str(i) for i in range(len(arrays))]  # give names to each columns
#     )
#     print(table)
#     #table = pa.array(matrix)
#
#
#     #assert False
#
#     # Save it:
#     pq.write_table(table, 'table.pq')
#
#     # Read it back as numpy:
#     table_from_parquet = pq.read_table('table.pq')
#     print(table_from_parquet)
#
#
#     matrix_from_parquet = table_from_parquet.to_pandas().T.values
#     print(matrix_from_parquet)
#
#     #assert False
#     #    .T.to_numpy()
#
#     assert np.allclose(matrix, matrix_from_parquet)
