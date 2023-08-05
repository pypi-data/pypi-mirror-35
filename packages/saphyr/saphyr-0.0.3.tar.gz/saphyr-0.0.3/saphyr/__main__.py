import click
import shutil
from git import Repo
import tempfile
import os

__author__ = "Guillaume Bailleul"


@click.group()
def main():
    """
    Saphyr Web Framework
    """
    pass


@main.command()
@click.argument('name')
def new(name):
    dirpath = tempfile.mkdtemp()
    repo = "https://github.com/laibulle/saphyr.git"

    Repo.clone_from(repo, dirpath)
    shutil.copytree(dirpath + "/saphyr_skeleton", name)
    shutil.rmtree(dirpath)

    for root, subdirs, files in os.walk(name):
        for subdir in subdirs:
            for filename in files:
                file_path = os.path.join(root, filename)
                f = open(file_path, 'r')
                f_content = f.read()
                f.close()

                f_content = f_content.replace("Saphyr Skeleton", name)
                f_content = f_content.replace("saphyr_skeleton", name)
                f_content = f_content.replace("SAPHYR_SKELETON", name.upper())
                f_content = f_content.replace(
                    'saphyr = {editable = true, path = "./.."}',
                    'saphyr = {git = "'+repo+'", editable=true}'
                )
                f = open(file_path, 'w')
                f.write(f_content)
                f.close()

    click.echo(name + " created!")


if __name__ == "__main__":
    main()
