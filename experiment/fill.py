from cvx.data.render import render

if __name__ == "__main__":
    # gain this dictionary through reflection
    # every table has a shortname, e.g. prices and a longer descriptive name
    # we use the shortname to name the variable referring to the code
    names = {"A": "AAA", "B": "BBB", "C": "CCC"}
    strategy = "s239"

    print(render(names, strategy))

    # open the template
    # template = Template(open("creator.py.jinja2").read())

    # we copy & paste the new class into a new file
    # print(template.render(names=names, strategy="s239"))
