"""Create a dataclass from a template"""
from jinja2 import Template

if __name__ == "__main__":
    # gain this dictionary through reflection
    # every table has a shortname, e.g. prices and a longer descriptive name
    # we use the shortname to name the variable refering to the code
    names = {"A": "AAA", "B": "BBB", "C": "CCC"}

    # open the template
    template = Template(open("creator.py.jinja2").read())

    # we copy & paste the new class into a new file
    print(template.render(names=names, strategy="s239"))
