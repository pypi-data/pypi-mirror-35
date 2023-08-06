import os
from pathlib import Path
from subprocess import call

import click

from lztools.git import list_files, load_file, save_file, _get_repo
from lztools.click import proper_group, proper_command
from builtins import list as blist
rpath = Path.home().joinpath(".lztools/resources").absolute()
opath = Path(".").absolute()

def ensure_repo():
    if not rpath.exists():
        rpath.parent.mkdir(parents=True, exist_ok=True)
        os.chdir(str(rpath.parent))
        call(["git", "clone", "git@bitbucket.org:zanzes/resources.git"])
        os.chdir(str(opath))

@proper_group()
def main():
    """Template bash command -h help text by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    ensure_repo()

@proper_command()
def list():
    files = blist(list_files(str(rpath)))
    for k, v in enumerate(files):
        print(f'{k}:\t{v.path}')

@proper_command()
def load():
    files = blist(list_files(str(rpath)))
    for k, v in enumerate(files):
        print(f'{k}:\t{v.path}')
    id = int(input("File #:\n"))
    load_file(str(rpath), files[id])

@proper_command()
@click.argument("PATH", default=click.get_text_stream('stdin'))
def save(path):
    save_file(str(rpath), path)