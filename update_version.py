import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))
init_path=os.path.join(here,"plotext", "__init__.py")
setup_path=os.path.join(here, "setup.py")

ver=""
with codecs.open(setup_path, 'r') as fp:
    lines=fp.read()
for line in lines.splitlines():
    if line.startswith('    version'):
        delim = '"' if '"' in line else "'"
        ver=line.split(delim)[1]

print("the current version is {}".format(ver))
print("please enter new version: ")
new_ver=input()

setup_line="""    version='"""+new_ver+"""',\n"""
with open(setup_path, "r") as f:
    lines = f.readlines()
with open(setup_path, "w") as f:
    for line in lines:
        if line.startswith("    version"):
            f.write(setup_line)
        else:
            f.write(line)

init_line="""__version__ = \""""+new_ver+"""\""""
with open(init_path, "r") as f:
    lines = f.readlines()
with open(init_path, "w") as f:
    for line in lines:
        if line.startswith("__version__"):
            f.write(init_line)
        else:
            f.write(line)

print("version {} updated.".format(new_ver))
