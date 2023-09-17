import codecs
from json import load
from pathlib import Path
from urllib.request import urlopen

import toml
from jinja2 import Template


def load_gist(gist_id):
    """translate Gist ID to URL"""
    gist_id = "a4a054e3e80a8021c351b027280d3b09"
    gist_api = urlopen("https://api.github.com/gists/" + gist_id)

    for name, data in load(gist_api)["files"].items():
        yield name, urlopen(data["raw_url"]).read().decode()


def write(file, output_file, **kwargs):
    # output the file
    output_file = codecs.open(root / output_file, "w", "utf-8")
    template = Template(file, trim_blocks=True)
    output_file.write(template.render(**kwargs))
    output_file.close()


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    d = toml.load(root / "pyproject.toml")
    name = d["tool"]["poetry"]["name"]
    repo = d["tool"]["poetry"]["repository"]

    files = dict(load_gist("a4a054e3e80a8021c351b027280d3b09"))

    write(files["Contributing.md"], "CONTRIBUTING.md", package=name, repo=repo)
    write(files["CodeOfConduct.md"], "CODE_OF_CONDUCT.md", package=name, repo=repo)
