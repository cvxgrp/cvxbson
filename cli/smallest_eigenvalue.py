import fire  # type: ignore
import numpy as np

from cvx.bson import read_bson


def smallest_ev(bson_file) -> None:
    """Print FILENAME if the file exists."""
    data = read_bson(bson_file)
    w, _ = np.linalg.eigh(data["cov"])
    return np.min(w)


def main():
    fire.Fire(smallest_ev)
