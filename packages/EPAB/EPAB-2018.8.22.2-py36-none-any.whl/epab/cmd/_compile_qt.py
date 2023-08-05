# coding=utf-8
"""
Updates CHANGELOG.rst with the latest commits
"""

import click

import epab.utils
from epab.core import CONFIG


@epab.utils.run_once
@epab.utils.stashed
def _compile_qt_resources():
    """
    Compiles PyQT resources file
    """
    if CONFIG.qt__res_src:
        epab.utils.ensure_exe('pyrcc5')
        epab.utils.info('Compiling Qt resources')
        epab.utils.run(f'pyrcc5 {CONFIG.qt__res_src} -o {CONFIG.qt__res_tgt}')


@click.command()
def compile_qt_resources():
    """
    Compiles PyQT resources file
    """
    _compile_qt_resources()
