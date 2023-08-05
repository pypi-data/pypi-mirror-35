from pathlib import Path
from shlex import quote
from fabkit.util import run_or_sudo
from fabric.operations import settings, hide


def is_file(path, use_sudo=False):
    return _test('-f', path, use_sudo)


def is_dir(path, use_sudo: False):
    return _test('-d', path, use_sudo)


def is_link(path, use_sudo: False):
    return _test('-L', path, use_sudo)


def exists(path, use_sudo: False):
    return _test('-e', path, use_sudo)


def chown(path, user=None, group=None, user_group=False, recursive=False, use_sudo=False):
    if isinstance(path, Path):
        path = str(path)
    if not user and not group:
        raise ValueError("[chown] One of user/group must be provided")
    if group:
        group = f':{group}'
    elif user_group:
        group = f':{user}'

    args = []
    if recursive:
        args.append('-R')

    args.append(f'{user}{group}')
    args = ' '.join(args)
    run_or_sudo(f'chown {args} {quote(path)}', use_sudo)


def mkdir(path, parent=True, use_sudo=False):
    if isinstance(path, Path):
        path = str(path)
    args = []
    if parent:
        args.append('-p')

    args = ' '.join(args)
    run_or_sudo(f'mkdir {args} {quote(path)}', use_sudo)


def _test(option, path, use_sudo):
    if isinstance(path, Path):
        path = str(path)

    with settings(hide('running', 'stdout', 'stderr', 'warnings'), warn_only=True):
        return run_or_sudo(f'test {option} {quote(path)}', use_sudo).succeeded
