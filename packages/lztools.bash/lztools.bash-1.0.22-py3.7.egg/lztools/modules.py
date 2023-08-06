#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from subprocess import CalledProcessError, check_output, call

import pip
import sh
from lztools.text import regex
from lztools.TempPath import TempPath

_setup_text = """#!/usr/bin/env python3.7
import codecs

from setuptools import setup

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {{True: enc}}.get(name=='mbcs')
    codecs.register(func)


setup(
    name='{fullname}',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='0.0.1',
    license='MIT License',
    description='A collection of useful utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙',
    url='',
    requires=["{packname}"],
    entry_points={{
        'console_scripts': [
            'l{module} = cli.l{module}:main',
        ],
    }},
    packages=['{packname}', 'cli', 'resources'],
    zip_safe=False,
    include_package_data=True,
    package_data={{'{fullname}': ['resources/*']}},
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],
)

"""
_readme_text = """# {fullname}

A collection of useful utilities by Laz aka Zanzes"""
_main_text = """def template():
    print("Hello, World!")"""
_command_text = """import click
from lztools.click import proper_group
from {fullname} import template

@proper_group()
@click.argument("TEMPLATE_ARGUMENT", default=click.get_text_stream('stdin'))
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(template_argument, verbose):
    \"\"\"Template bash command by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙\"\"\"
    if verbose:
        print("Calling main functions")
    template()
    if verbose:
        print("Handling TEMPLATE_ARGUMENT")
    if template_argument:
        print(f"TEMPLATE_ARGUMENT: {{template_argument}}")"""
packs_text = """#!/usr/bin/env python3.7

pip_requires = [
    "click"
]

apt_requires = [
]
"""
license_text = """Copyright (c) 2016 The Python Packaging Authority (PyPA)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
setup_text = """[metadata]
# This includes the license file in the wheel.
license_file = LICENSE.txt

[bdist_wheel]
# This flag says to generate wheels that support both Python 2 and Python
# 3. If your code will not run unchanged on both Python 2 and 3, you will
# need to generate separate wheels for each Python version that you
# support. Removing this line (or setting universal to 0) will prevent
# bdist_wheel from trying to make a universal wheel. For more see:
# https://packaging.python.org/tutorials/distributing-packages/#wheels
universal=1
"""

def extract_module_version(text):
    return regex(" \d+\.\d+\.\d+", text, only_first=True)[1:]

def set_version(original, new):
    new = check_output(["cat", "setup.py"]).decode("utf8").replace(original, new)
    with open("setup.py", "w") as f:
        f.write(new)

def add_versions(left, right):
    l1, l2, l3 = left.split(".")
    r1, r2, r3 = right.split(".")
    e1, e2, e3 = int(l1) + int(r1), int(l2) + int(r2), int(l3) + int(r3),
    return f"{e1}.{e2}.{e3}"

def clean():
    call(["rm", "-rf", "*egg-info"])
    call(["rm", "-rf", "build", "dist", "*.egg-info"])
    for x in Path(".").glob("*.egg*"):
        print(x)
        call(["rm", "-rf", str(x.absolute())])

def local_install(path, upload=False, add_to_version=None, password=None):
    with TempPath(path):
        clean()
        if add_to_version is not None:
            ov = get_version()
            nv = add_versions(ov, add_to_version)
            set_version(ov, nv)
        call(["python3.7", "setup.py", "install"])
        clean()
        if upload:
            call(["python3.7", "setup.py", "install", "sdist", "bdist_wheel"])
            _upload(password)
        clean()

def get_name_from_path():
    _, end = check_output(["cat", "setup.py"]).decode("utf8").split("name='", 1)
    name, _ = end.split("'", 1)
    return name

def _upload(password):
    online = get_version_online(get_name_from_path())
    local = get_version()
    if online == local:
        raise Exception("Error: Same version as online")
    else:
        twine = sh.twine.bake(_cwd=".")
        print(twine.upload("dist/*", username="zanzes", password=password))
        #call(["twine", "upload", "-u", "zanzes", "dist/*", *parg])

def get_version_online(name):
    try:
        out = check_output(["python3.7", "-m", "pip", "search", "-V", "--no-cache-dir", name]).decode("utf8")
        _, end = out.split(f"{name} (", 1)
        version, _ = end.split(")", 1)
        return version
    except CalledProcessError:
        return "-999"

def get_version():
    return check_output(["python3.7", "setup.py", "-V"]).decode("utf8").rstrip("\n")

def pip_install(package):
    pip.main(['install', package])

def _create_data(name, pack=""):
    packd = ""
    if pack != "":
        packd = pack+"."
    pname = name if pack == "" else pack
    data = {
        "fullname": packd+name,
        "packname": pname,
        "module": name
    }
    return data

def create_new(name, pack=""):
    data = _create_data(name, pack)
    def mf(file:Path, text:str):
        file.touch()
        with file.open("w") as f:
            f.write(text)
    pack = Path(name)
    pack.mkdir()

    res = pack.joinpath("resources")
    res.mkdir()

    packs = res.joinpath("packs.py")
    mf(packs, packs_text)

    license = pack.joinpath("LICENSE.txt")
    mf(license, license_text)

    setupcfg = pack.joinpath("setup.cfg")
    mf(setupcfg, setup_text)

    # call(["rm", "-rf", name+"/resources/__pycache__"])
    setup = pack.joinpath("setup.py")
    mf(setup, _setup_text.format(module=data["module"], fullname=data["fullname"], packname=data["packname"]))

    readme = pack.joinpath("README.md")
    mf(readme, _readme_text.format(fullname=data["fullname"]))

    inner = pack.joinpath(data["packname"])
    inner.mkdir()
    main = inner.joinpath(data["module"]+".py")
    mf(main, _main_text)

    cli = pack.joinpath("cli")
    cli.mkdir()
    command = cli.joinpath("l"+data["module"]+".py")
    mf(command, _command_text.format(fullname=data["fullname"]))




