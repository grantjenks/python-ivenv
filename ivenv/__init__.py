"""
Interactive Virtual Environments
================================

"""

import os
import pathlib
import site
import sys

BIN_NAME = 'bin'
SITE_PACKAGES_GLOB = '*/site-packages'


def activate(path):
    """Activate virtual environment at `path`.

    """
    # TODO: Add heuristics/features for finding venv directory:
    # - Expand home dir
    # - Expand environment variables
    # - Support path relative to file
    venv_path = pathlib.Path(path)
    # TODO: emit warning if Python versions do not match
    venv_dir = venv_path.resolve(strict=True)

    # Update PATH environment variable.

    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    venv_bin_dir = venv_dir / BIN_NAME
    path_dirs.insert(0, str(venv_bin_dir))
    os.environ["PATH"] = os.pathsep.join(path_dirs)

    # Update VIRTUAL_ENV environment variable.

    os.environ["VIRTUAL_ENV"] = str(venv_dir)

    # Record the length of the path to move the added paths from the end to the
    # beginning.

    path_len = len(sys.path)

    # Find site packages paths.

    site_paths = list((venv_dir / 'lib').glob(SITE_PACKAGES_GLOB))
    for site_path in site_paths:
        site.addsitedir(site_path)

    # Move the sys paths added at the end back to the beginning.

    sys.path[:] = sys.path[path_len:] + sys.path[:path_len]

    # Update sys prefix attributes.

    sys.real_prefix = sys.prefix
    sys.prefix = str(venv_dir)


def deactivate():
    pass


__title__ = 'ivenv'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = '2020, Grant Jenks'
