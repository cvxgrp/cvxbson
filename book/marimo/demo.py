import marimo

__generated_with = "0.9.27"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(r"""# cvxbson""")
    return


@app.cell
def __():
    import numpy as np

    from src.cvx.bson import read_bson, write_bson
    from src.cvx.json import read_json, write_json

    return np, read_bson, read_json, write_bson, write_json


@app.cell
def __(mo):
    mo.md(r"""## Create a dictionary of numpy arrays""")
    return


@app.cell
def __(np):
    data = {"A": np.random.rand(50, 50), "B": np.random.rand(50)}
    return (data,)


@app.cell
def __(mo):
    mo.md(r"""## json""")
    return


@app.cell
def __(data, np, read_json, write_json):
    write_json("test.json", data)
    _recovered = dict(read_json("test.json"))
    assert np.allclose(data["A"], _recovered["A"])
    assert np.allclose(data["B"], _recovered["B"])
    return


@app.cell
def __(mo):
    mo.md(r"""## bson""")
    return


@app.cell
def __(data, np, read_bson, write_bson):
    write_bson("test.bson", data)
    _recovered = dict(read_bson("test.bson"))
    assert np.allclose(data["A"], _recovered["A"])
    assert np.allclose(data["B"], _recovered["B"])
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
