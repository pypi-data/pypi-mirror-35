import importlib
import os
from collections import namedtuple
from datetime import datetime
from subprocess import call
from importlib import util


import sh

GitFileData = namedtuple("GitFileData", ["permissions", "type", "hash", "path"])

repos = dict()

def _get_repo(path):
    if path not in repos:
        repos[path] = sh.git.bake(_cwd=path)
    return repos[path]

def save_file(repo, file:str):
    call(["cp", file, repo + "/" + file])
    _get_repo(repo).add(file)
    _get_repo(repo).commit(file, "-m", f"\"{datetime.now()}\"")
    _get_repo(repo).push()

def load_file(repo, file:GitFileData):
    """git checkout HEAD -- {path}"""
    try:
        _get_repo(repo).checkout("master", "--", file.path)
        # print("Successfully loaded: {}".format(file.path))
    except Exception as e:
        raise Exception("There was an error checking out file: {}\n{}".format(file.path, e))
    call(["cp", "-v", repo+"/" + file.path, "."])

def list_files(repo, filter=None, branch="master"):
    """git ls-tree -r master --name-only"""
    files = _get_repo(repo)('ls-tree', "-r", branch).stdout.decode("utf8").strip().splitlines()
    for data in files:
        split, file = data.split("\t")
        if filter is None or filter in file:
            permissions, type, hash = split.split(" ")
            yield GitFileData(permissions, type, hash, file)

def clone_repo(url, name=None):
    args = ["git", "clone", url]
    if name is not None:
        args.append(name)
    call(args)

def clone_repo_on_id(id, name=None):
    p = __file__.rsplit(os.sep, 2)[0] + "/resources/KnownRepos.py"
    KnownReposSpec = util.spec_from_file_location("KnownRepos", p)
    KnownRepos = util.module_from_spec(KnownReposSpec)
    KnownReposSpec.loader.exec_module(KnownRepos)
    url = KnownRepos.KnownRepos[id]
    clone_repo(url, name)

