import os
import tempfile
import traceback
import uuid
import functools

import pytest
import click.testing
import git

from ginteract import main


@pytest.fixture()
def runner():
    return click.testing.CliRunner() 


def check(f):
    @functools.wraps(f)
    def w(*args, **kwargs):
        result = f(*args, **kwargs)
        if result.exit_code == 0:
            return
        
        etype, value, tb = result.exc_info
        print(''.join(traceback.format_exception(etype, value, tb)))
        raise Exception('Exit code is {}'.format(result.exit_code))
    
    return w


def make_commit(repo: git.Repo):
    filename = str(uuid.uuid4())
    path = os.path.join(os.path.dirname(repo.git_dir), filename)
    with open(path, 'w') as fp:
        fp.write(filename)  # write filename to file for fun

    repo.index.add([path])
    repo.git.commit('-m', filename)


@pytest.fixture()
def repo():
    tmpdir = tempfile.TemporaryDirectory()
    os.chdir(tmpdir.name)

    repo = git.Repo.init(tmpdir.name)
    make_commit(repo)

    repo.create_head('branch0')
    make_commit(repo)

    repo.create_head('branch1')
    make_commit(repo)

    yield repo

    os.chdir(os.path.dirname(__file__))
    tmpdir.cleanup()


@check
def test_checkout(runner, repo):
    result = runner.invoke(main.checkout, input='branch0')
    assert str(repo.active_branch) == 'branch0'
    return result


@check
def test_checkout_with_arg(runner, repo):
    result = runner.invoke(main.checkout, args=['branch0'])
    assert str(repo.active_branch) == 'branch0'
    return result


@check
def test_merge(runner, repo):
    repo.git.checkout('master')
    result = runner.invoke(main.merge, input='branch1')
    assert 3 == len(list(repo.iter_commits('master')))
    return result


@check
def test_delete(runner, repo):
    result = runner.invoke(main.delete, input='branch0 branch1\ny')
    assert 1 == len(repo.branches)
    return result
