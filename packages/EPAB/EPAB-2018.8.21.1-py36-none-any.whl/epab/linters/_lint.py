# coding=utf-8
"""
Runs all linters
"""
import click

import epab.utils
from epab.core import CTX

from ._flake8 import flake8
from ._mypy import mypy
from ._pep8 import pep8
from ._pylint import pylint
from ._safety import safety
from ._sort import sort


@epab.utils.run_once
@epab.utils.stashed
def _lint(ctx: click.Context, amend: bool = False, stage: bool = False):
    epab.utils.info('Running all linters')
    ctx.invoke(safety)
    ctx.invoke(pylint)
    ctx.invoke(flake8)
    ctx.invoke(mypy)
    ctx.invoke(pep8, amend=amend, stage=stage)
    if not CTX.appveyor:
        ctx.invoke(sort, amend=amend, stage=stage)


@click.command()
@click.pass_context
@click.option('-a', '--amend', is_flag=True, help='Amend last commit with changes')
@click.option('-s', '--stage', is_flag=True, help='Stage changed files')
def lint(ctx: click.Context, amend: bool = False, stage: bool = False):
    """
    Runs all linters

    Args:
        ctx: click context
        amend: whether or not to commit results
        stage: whether or not to stage changes
    """
    _lint(ctx, amend, stage)
