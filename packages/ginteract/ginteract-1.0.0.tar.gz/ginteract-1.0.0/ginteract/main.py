import functools
import os
import sys

import click
import git

from ginteract import interact


@click.group()
def main():
    pass


def command(f):
    @click.command()
    @functools.wraps(f)
    def wrapper(**kwargs):
        repo = git.Repo(os.getcwd(), search_parent_directories=True)

        # noinspection PyTypeChecker
        branches = sorted(repo.branches, key=lambda branch: branch.commit.committed_date, reverse=True)
        branches = [str(branch) for branch in branches]
        current = str(repo.active_branch)
        branches = list(filter(lambda branch: branch != current, branches))
        cmd = f(repo, branches, current, **kwargs)
        try:
            cmd()
        except git.exc.GitCommandError as e:
            click.echo(e)

    main.add_command(wrapper)
    return wrapper


@command
@click.argument('args', nargs=-1)
def checkout(repo, branches, current, args):
    if not args:
        choice = interact.prompt(branches, current=current)
        args = [choice]

    return lambda: repo.git.checkout(*args)


@command
def merge(repo, branches, current):
    choice = interact.prompt(branches, '{} <- '.format(current))
    return lambda: repo.git.merge(choice)


@command
def delete(repo, branches, _):
    choices = interact.prompt(branches, multiple=True)
    if choices and not click.confirm('Delete {}?'.format(', '.join(choices))):
        raise click.Abort

    def delete_branches():
        for branch in choices:
            repo.git.branch('-d', branch)

    return delete_branches


if __name__ == '__main__':
    sys.exit(main())
