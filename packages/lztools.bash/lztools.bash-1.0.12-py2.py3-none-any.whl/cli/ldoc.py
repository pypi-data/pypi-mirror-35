#!/usr/bin/env python3

import click

from lztools.docker import get_running
from lztools.click import proper_group, proper_command

@proper_group()
def main():
    """A collection of python tools and bash commands for git by Laz aka nea"""
    pass

@proper_command()
@click.option("-a" "--all", is_flag=True, default=True)
@click.option("-l" "--list", is_flag=True, default=True)
def kill():
    """test"""
    get_running()
    pass

@proper_command()
@click.option("-a" "--all", is_flag=True, default=True)
def run():
    """test"""
    pass

