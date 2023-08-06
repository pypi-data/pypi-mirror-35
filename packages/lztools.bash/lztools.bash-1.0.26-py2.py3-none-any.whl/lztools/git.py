from collections import namedtuple
from datetime import datetime
from subprocess import call

import sh

GitFileData = namedtuple("GitFileData", ["permissions", "type", "hash", "path"])

repos = dict()

def get_repo(path):
    if path not in repos:
        repos[path] = sh.git.bake(_cwd=path)
    return repos[path]

def save_file(repo, file:str, remove_original=False):
    cmd = "mv" if remove_original else "cp"
    call([cmd, file, repo + "/" + file])
    repo = get_repo(repo)
    repo.add(file)
    repo.commit(file, "-m", f'"{datetime.now()}"')
    repo.push()

def load_file(repo, file:GitFileData):
    """git checkout HEAD -- {path}"""
    try:
        get_repo(repo).checkout("master", "--", file.path)
        # print("Successfully loaded: {}".format(file.path))
    except Exception as e:
        raise Exception("There was an error checking out file: {}\n{}".format(file.path, e))
    call(["cp", "-vr", repo+"/" + file.path, "."])

def list_files(repo, filter=None, branch="HEAD"):
    """git ls-tree -r -t HEAD/{branch} --name-only"""
    files = get_repo(repo)('ls-tree', "-r", "-t", branch).stdout.decode("utf8").strip().splitlines()
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

# def select_file():
#     pairs = {}
#     for k, v in enumerate(list_files(str(resources_path))):
#         print(f'{k}:\t{v.path}')
#         pairs[k] = v
#     id = int(input("File #:\n"))
#     return pairs[id]

