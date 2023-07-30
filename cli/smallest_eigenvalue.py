import fire  # type: ignore
import numpy as np

from cvx.bson import read_bson


def smallest_ev(bson_file) -> None:
    """
    Compute the smallest eigenvalue of a matrix stored in a bson file.
    The key for the matrix shall be "cov".

    There are faster methods to compute the smallest eigenvalue, e.g. inverse power iteration.
    Here, we only use this as an example to work with the bson interface

    On the command line

    poetry run smallest-eigenvalue cli/data/test.bson
    """
    matrix = read_bson(bson_file)["cov"]
    w, _ = np.linalg.eigh(matrix)
    return np.min(w)


def main():
    fire.Fire(smallest_ev)
