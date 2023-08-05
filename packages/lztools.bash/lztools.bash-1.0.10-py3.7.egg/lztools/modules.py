#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from subprocess import CalledProcessError, check_output, call

import pip
import sh
from lztools.text import regex
from lztools.TempPath import TempPath

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
            try:
                _upload(password)
            except:
                raise
            finally:
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
    p = __file__.rsplit(os.sep, 2)[0]+"/resources"
    call(["cp", "-rfp", p + "/resources", name+"/."])
    call(["cp", "-rfp", p + "/LICENSE.txt", name+"/."])
    call(["cp", "-rfp", p + "/setup.cfg", name+"/."])
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




