# coding=utf-8
"""
iSort linter
"""
from pathlib import Path

import click
import isort

import epab.core
import epab.utils


def _sort_file(file_path: Path):
    try:
        isort.SortImports(
            file_path=file_path.absolute(),
            known_first_party=epab.core.CONFIG.package,
            **SETTINGS
        )
    except UnicodeDecodeError:
        raise RuntimeError(f'failed to decode file: {file_path}')


SETTINGS = {
    'line_ending': '\n',
    'line_length': int(epab.core.CONFIG.lint__line_length),
}


@epab.utils.run_once
@epab.utils.stashed
def _sort(amend: bool = False, stage: bool = False):
    for py_file in Path(f'./{epab.core.CONFIG.package}').rglob('*.py'):
        _sort_file(py_file)
    for py_file in Path('./test').rglob('*.py'):
        _sort_file(py_file)

    if amend:
        epab.core.CTX.repo.amend_commit(append_to_msg='sorting imports [auto]')
    elif stage:
        epab.core.CTX.repo.stage_all()


@click.command()
@click.option('-a', '--amend', is_flag=True, help='Amend last commit with changes')
@click.option('-s', '--stage', is_flag=True, help='Stage changed files')
def sort(amend: bool = False, stage: bool = False):
    """
    Runs iSort (https://pypi.python.org/pypi/isort)

    Args:
        amend: whether or not to commit results
        stage: whether or not to stage changes
    """
    _sort(amend, stage)
