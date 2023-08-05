# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['structlogger']

package_data = \
{'': ['*']}

install_requires = \
['python-json-logger>=0.1.9,<0.2.0', 'structlog[dev]>=18.1,<19.0']

setup_kwargs = {
    'name': 'structlogger',
    'version': '0.1.3',
    'description': 'Uses structlog to create two loggers, a stdout logger with key-value args and optional colour, and a file logger in JSON format with log-rotation.',
    'long_description': "StructLogger |Version| |Docs|\n=============================\n\n|Compatibility| |Implementations| |Format| |Code_Style|\n\nUses structlog to create two loggers, a stdout logger with key-value args and optional colour, and a \nfile logger in JSON format with log-rotation.\n\n\nDocumentation\n-------------\nStructLogger's documentation can be found at `https://structlogger.readthedocs.io <https://structlogger.readthedocs.io>`_\n\n\nInstalling StructLogger\n-----------------------\nStructLogger can be installed from Pypi using pip::\n\n    pip install structlogger\n\n\nExample\n-------\n\nStructLogger defines a set of standard parameters that should get you going quickly and easily. Settings are retrofitted to \nthe standard logging module to ensure any of your dependencies will adhere to the same logging format.\n\n.. code :: python\n\n   import structlog\n   from structlogger import configure_logger, __version__\n\n   configure_logger()\n\n   log = structlog.getLogger()\n\n   log.info('Welcome to structlogger', version=__version__)\n\n.. |Version| image:: https://img.shields.io/pypi/v/structlogger.svg\n   :target: https://pypi.python.org/pypi/structlogger\n.. |Docs| image:: https://readthedocs.org/projects/structlogger/badge/?version=latest\n   :target: https://structlogger.readthedocs.io\n.. |Compatibility| image:: https://img.shields.io/pypi/pyversions/structlogger.svg\n   :target: https://pypi.python.org/pypi/structlogger\n.. |Implementations| image:: https://img.shields.io/pypi/implementation/structlogger.svg\n   :target: https://pypi.python.org/pypi/structlogger\n.. |Format| image:: https://img.shields.io/pypi/format/structlogger.svg\n   :target: https://pypi.python.org/pypi/structlogger\n.. |Code_Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n",
    'author': 'Matt Davis',
    'author_email': 'mattdavis90@googlemail.com',
    'url': 'https://github.com/mattdavis90/structlogger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
