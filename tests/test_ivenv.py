"""Tests for ivenv

"""

import sys

from pathlib import Path
from shutil import rmtree
from subprocess import run
from tempfile import mkdtemp

import pytest

import ivenv


def test_ivenv():
    # Make sure numpy is not installed.
    with pytest.raises(ImportError):
        import numpy

    # Create temporary directory for virtual environment.
    tempdir = mkdtemp()

    # Create virtual environment and install numpy.
    venv_dir = Path(tempdir) / 'env'
    python = ['python', '-I', '-m']
    run([*python, 'venv', str(venv_dir)])
    run([*python, 'pip', 'install', '--prefix', str(venv_dir), 'numpy'])

    # Make sure numpy was installed into the new virtual environment.
    with pytest.raises(ImportError):
        import numpy

    # Activate the new virtual environment and import numpy.
    ivenv.activate(venv_dir)
    import numpy
    assert numpy.__version__

    # "Un-import" numpy and deactivate the virtual environment.
    del numpy
    del sys.modules['numpy']
    ivenv.deactivate()

    # Make sure numpy cannot be imported now.
    with pytest.raises(ImportError):
        import numpy

    # Remove temporary directory.
    rmtree(tempdir, ignore_errors=True)
