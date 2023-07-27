import fire  # type: ignore
import numpy as np

from cvx.bson import read_bson


def smallest_ev(bson_file) -> None:
    """Print FILENAME if the file exists."""
    data = read_bson(bson_file)

    #    json_data = json.load(f)

    # a_restored = np.asarray(json_data["a"])

    w, v = np.linalg.eigh(data["cov"])
    idx = w.argsort()
    w = w[idx]
    return w[0]


def main():
    fire.Fire(smallest_ev)
