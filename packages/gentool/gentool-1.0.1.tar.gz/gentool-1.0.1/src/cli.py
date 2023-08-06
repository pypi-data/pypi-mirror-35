#!/usr/bin/env python
""" CLI commands
"""
import click
import os
from src.scripts import *
from src.misc import *
from src.utils.decorators import *

@click.group()
def gentool():
    pass


@gentool.command()
@click.argument("source", type=click.Path(writable=True, resolve_path=True))
@click.argument("target", required=False, type=click.Path(writable=True, resolve_path=True))
@click.argument("filters", required=False, type=click.STRING)
@transform_args('str')
def mva(source=os.getcwd(), target=os.getcwd(), filters="**/"):
    """ Move a group files from a directory

    """
    click.echo("move all files")
    move_files(source, target, filters)


@gentool.command()
@click.argument("source", type=click.Path())
@click.argument("target", required=False, type=click.Path())
@transform_args('str')
def mv(source, target):
    click.echo("move file")
    move_file(source, target)


@gentool.command()
@click.argument("source", type=click.Path())
@click.argument("target", required=False, type=click.Path())
@click.argument("filters", required=False)
@transform_args('str')
def cpa(source, target, filters="**/"):
    #click.echo("copy all files")
    copy_files(str(source), str(target), str(filters))
    click.echo("copy all files")


@gentool.command()
@click.argument("source", type=click.Path())
@click.argument("target", required=False, type=click.Path())
@transform_args('str')
def cp(source, target=os.getcwd()):
    click.echo("copy file")
    copy_file(source, target)


@gentool.command()
@click.argument("source", type=click.Path())
@click.argument("target", required=False, type=click.Path())
def unzip( source, target = os.getcwd()):
    click.echo("unzip a single ")
    unzip_folder(source, target)


@gentool.command()
@click.argument("source", type=click.Path())
@click.argument("target", required=False, type=click.Path())
@transform_args('str')
def unzipa(source, target):
    click.echo("Unzip all zip folders")
    unzip_folders(source, target)


@gentool.command()
@click.argument("lower_limit", nargs=1)
@click.argument("upper_limit", nargs=1, required=False)
def log(lower_limit, upper_limit):
    log_num(lower_limit, upper_limit)

if __name__ ==  "__main__":
    gentool()
