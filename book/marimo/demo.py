"""Marimo notebook demonstrating cvxbson functionality for JSON and BSON serialization."""

import marimo

__generated_with = "0.9.27"
app = marimo.App()

with app.setup:
    import marimo as mo
    import numpy as np

    from cvx.bson import read_bson, write_bson
    from cvx.json import read_json, write_json


@app.cell
def title():
    """Display the title of the notebook."""
    mo.md(r"""# cvxbson""")
    return


@app.cell
def create_data_header():
    """Display the header for creating data section."""
    mo.md(r"""## Create a dictionary of numpy arrays""")
    return


@app.cell
def create_data():
    """Create sample data for demonstration."""
    data = {"A": np.random.rand(50, 50), "B": np.random.rand(50)}
    return (data,)


@app.cell
def json_header():
    """Display the header for JSON section."""
    mo.md(r"""## json""")
    return


@app.cell
def test_json(data):
    """Test JSON serialization and deserialization."""
    write_json("test.json", data)
    _recovered = dict(read_json("test.json"))
    assert np.allclose(data["A"], _recovered["A"])
    assert np.allclose(data["B"], _recovered["B"])
    return


@app.cell
def bson_header():
    """Display the header for BSON section."""
    mo.md(r"""## bson""")
    return


@app.cell
def test_bson(data):
    """Test BSON serialization and deserialization."""
    write_bson("test.bson", data)
    _recovered = dict(read_bson("test.bson"))
    assert np.allclose(data["A"], _recovered["A"])
    assert np.allclose(data["B"], _recovered["B"])
    return


if __name__ == "__main__":
    app.run()
