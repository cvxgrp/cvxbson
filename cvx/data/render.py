#    Copyright 2023 Stanford University Convex Optimization Group
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""Create a dataclass from a template"""
from pathlib import Path

from jinja2 import Template


def render(names, strategy):
    # gain this dictionary through reflection
    # every table has a shortname, e.g. prices and a longer descriptive name
    # we use the shortname to name the variable refering to the code
    # names = {"A": "AAA", "B": "BBB", "C": "CCC"}
    path = Path(__file__).parent

    # open the template
    template = Template(open(path / "data_api.py.jinja2", encoding="utf-8").read())

    # we copy & paste the new class into a new file
    return template.render(names=names, strategy=strategy)
