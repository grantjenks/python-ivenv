ivenv: Interactive Virtual Environments
=======================================

`ivenv`_ is an Apache2 licensed Python module for interactive virtual
environments.

The `virtualenv` package had a clever script called `activate_this.py` which
when executed in a Python shell would "activate" the virtual
environment. Sadly, `venv` lacks this feature so `ivenv` adds it back.

The `ivenv` package also adds support for "%activate" and "%deactivate" magic
commands in IPython shells and Jupyter notebooks. This provides a simpler
alternative to installing `ipykernel` in the destination virtual environment
and adding the kernel to Jupyter.


Features
--------

- Pure-Python
- IPython Support
- Jupyter Support
- Developed on Python 3.8
- Tested on CPython 3.6, 3.7, 3.8 and PyPy, PyPy3
- Tested using GitHub Actions

.. image:: https://github.com/grantjenks/python-ivenv/workflows/integration/badge.svg
   :target: http://www.grantjenks.com/docs/ivenv/


Quickstart
----------

Installing `ivenv`_ is simple with `pip <http://www.pip-installer.org/>`_::

  $ pip install ivenv

You can access documentation in the interpreter with Python's built-in help
function:

.. code-block:: python

   >>> import ivenv
   >>> help(ivenv)
   >>> help(ivenv.activate)
   >>> help(ivenv.deactivate)


Tutorial
--------

The `ivenv`_ module provides two functions for managing virtual environments:

.. code-block:: python

   >>> from ivenv import activate, deactivate

The `activate` function accepts a path to a virtual environment directory and
"activates" that virtual environment within the Python shell.

.. code-block:: python

   >>> activate('path/to/venv/directory')

The `deactivate` function takes no arguments and "deactivates" the virtual
environment within the Python shell.

.. code-block:: python

   >>> deactivate()

It's also possible to use `ivenv`_ from IPython or Jupyter notebooks. To begin,
load the `ivenv` extension:

.. code-block:: shell

   %load_ext ivenv

Once the extension is loaded, the "magic" commands: `%activate` and
`%deactivate` may be used just as their corresponding functions.

.. code-block:: shell

   %activate path/to/venv/directory
   %deactivate


Reference
---------

* `ivenv Documentation`_
* `ivenv at PyPI`_
* `ivenv at GitHub`_
* `ivenv Issue Tracker`_

.. _`ivenv Documentation`: http://www.grantjenks.com/docs/ivenv/
.. _`ivenv at PyPI`: https://pypi.python.org/pypi/ivenv/
.. _`ivenv at GitHub`: https://github.com/grantjenks/python-ivenv/
.. _`ivenv Issue Tracker`: https://github.com/grantjenks/python-ivenv/issues/


License
-------

Copyright 2020 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.

.. _`ivenv`: http://www.grantjenks.com/docs/ivenv/
