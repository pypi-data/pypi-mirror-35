from builtins import list as blist

import click
from lztools.click import proper_group, proper_command
from lztools.git import list_files, load_file, save_file

from lztools import ResourceManager
from lztools.ResourceManager import resources_path

@proper_group()
def main():
    """Template bash command -h help text by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""

@proper_command()
@click.option("-f", "--force", "--override", is_flag=True, default=False)
def initialize(override):
    ResourceManager.ensure_initialized(override=override)

@proper_command()
def list():
    files = blist(list_files(str(resources_path)))
    for k, v in enumerate(files):
        print(f'{k}:\t{v.path}')

@proper_command()
def load():
    files = blist(list_files(str(resources_path)))
    for k, v in enumerate(files):
        print(f'{k}:\t{v.path}')
    id = int(input("File #:\n"))
    load_file(str(resources_path), files[id])

@proper_command()
@click.argument("PATH", default=click.get_text_stream('stdin'))
def save(path):
    save_file(str(resources_path), path)