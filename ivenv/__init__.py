"""
Interactive Virtual Environments
================================

"""

import os
import pathlib
import platform
import site
import sys

from typing import List, NamedTuple

if platform.system() == 'Windows':
    BIN_DIR = 'Scripts'
    LIB_DIR = 'Lib'
    SITE_PACKAGES_GLOB = 'site-packages'
else:
    BIN_DIR = 'bin'
    LIB_DIR = 'lib'
    SITE_PACKAGES_GLOB = '*/site-packages'


class _State(NamedTuple):
    """Virtual environment state.

    """
    os_path: str
    os_virtual_env: str
    sys_path: List[str]
    sys_prefix: str
    sys_exec_prefix: str

    @classmethod
    def get(cls):
        """Get state from `os` and `sys` settings.

        """
        return _State(
            os_path=os.environ.get('PATH'),
            os_virtual_env=os.environ.get('VIRTUAL_ENV'),
            sys_path=sys.path.copy(),
            sys_prefix=sys.prefix,
            sys_exec_prefix=sys.exec_prefix,
        )

    def set(self):
        """Set `os` and `sys` settings from state.

        """
        self._set_environ('PATH', self.os_path)
        self._set_environ('VIRTUAL_ENV', self.os_virtual_env)
        sys.path[:] = self.sys_path
        sys.prefix = self.sys_prefix
        sys.exec_prefix = self.sys_exec_prefix

    @staticmethod
    def _set_environ(key, value):
        if value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = value


class IVenv:
    """Interactive Virtual Environments

    """
    def __init__(self):
        start_state = _State.get()
        self._stack: List[_State] = [start_state]

    def activate(self, path):
        """Activate virtual environment at `path`.

        """
        # IDEA: Add heuristics/features for finding venv directory:
        # - Support path relative to file
        vars_path = os.path.expandvars(path)
        user_path = os.path.expanduser(vars_path)
        venv_path = pathlib.Path(user_path)
        venv_dir = venv_path.resolve(strict=True)
        # IDEA: emit warning if Python versions do not match
        state = _State(
            os_path=self._make_os_path(venv_dir),
            os_virtual_env=str(venv_dir),
            sys_path=self._make_sys_path(venv_dir),
            sys_prefix=str(venv_dir),
            sys_exec_prefix=str(venv_dir),
        )
        state.set()
        self._stack.append(state)

    @staticmethod
    def _make_os_path(venv_dir):
        path_dirs = os.environ.get('PATH', "").split(os.pathsep)
        venv_bin_dir = venv_dir / BIN_DIR
        path_dirs.insert(0, str(venv_bin_dir))
        os_path = os.pathsep.join(path_dirs)
        return os_path

    @staticmethod
    def _make_sys_path(venv_dir):
        path_len = len(sys.path)
        site_paths = (venv_dir / LIB_DIR).glob(SITE_PACKAGES_GLOB)
        for site_path in site_paths:
            site.addsitedir(site_path)
        sys_path = sys.path[path_len:] + sys.path[:path_len]
        return sys_path

    def deactivate(self):
        """Deactivate virtual environment.

        If no virtual environment is active, settings are restored to their
        startup state.

        """
        if len(self._stack) > 1:
            self._stack.pop()
        state = self._stack[-1]
        state.set()


_ivenv = IVenv()
activate = _ivenv.activate
deactivate = _ivenv.deactivate


__title__ = 'ivenv'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = '2020, Grant Jenks'
