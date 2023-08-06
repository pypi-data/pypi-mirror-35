# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
"""Copyright ©  2018 Justin Stout <justin@jstout.us>."""
import os

from pathlib import Path

from invoke import task


@task()
def twine(ctx, username, password):
    """Upload build files to pypi or devpi archive."""
    os.environ['TWINE_USERNAME'] = username
    os.environ['TWINE_PASSWORD'] = password

    dist_dir = Path('src/{}/dist'.format(ctx.app.pkg_name))
    cmd = 'twine upload {}/*'.format(dist_dir)
    ctx.run(cmd)
