from datetime import datetime
from subprocess import call

import sh
from lztools.git import GitFileData

from lztools import ResourceManager
from lztools.ResourceManager import resources_path as vault_path

_vault_repo = sh.git.bake(_cwd=vault_path)

def add_file(file:str, remove_original=False):
    ResourceManager.ensure_initialized()
    cmd = "mv" if remove_original else "cp"
    call([cmd, file, str(vault_path) + "/" + file])
    _vault_repo.add(file)
    _vault_repo.commit(file, "-m", f'"{datetime.now()}"')
    _vault_repo.push()

def load_file(file:GitFileData):
    """git checkout HEAD -- {path}"""
    try:
        _vault_repo.checkout("master", "--", file.path)
        # print("Successfully loaded: {}".format(file.path))
    except Exception as e:
        raise Exception("There was an error checking out file: {}\n{}".format(file.path, e))
    call(["cp", "-vr", str(vault_path)+"/" + file.path, "."])

def list_files(filter=None, branch="HEAD"):
    """git ls-tree -r -t HEAD/{branch} --name-only"""
    files = _vault_repo('ls-tree', "-r", "-t", branch).stdout.decode("utf8").strip().splitlines()
    for data in files:
        split, file = data.split("\t")
        if filter is None or filter in file:
            permissions, type, hash = split.split(" ")
            yield GitFileData(permissions, type, hash, file)

def select_file():
    pairs = {}
    for k, v in enumerate(list_files(str(vault_path))):
        print(f'{k}:\t{v.path}')
        pairs[k] = v
    id = int(input("File #:\n"))
    return pairs[id]

def clone_repo(url, name=None):
    args = ["git", "clone", url]
    if name is not None:
        args.append(name)
    call(args)