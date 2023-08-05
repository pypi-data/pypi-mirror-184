# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meizi']

package_data = \
{'': ['*'], 'meizi': ['templates/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'flask>=2.2.2,<3.0.0',
 'loguru>=0.6.0,<0.7.0',
 'parsel>=1.7.0,<2.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['mz = meizi.cli:cli']}

setup_kwargs = {
    'name': 'meizi',
    'version': '0.1.0',
    'description': '',
    'long_description': '====\nMeiz\n====\n\n*Meiz* provides two commands:\n\n- ``mz download`` for downloading nice albums.\n- ``mz serve`` for starting a simple web UI to serve the albums.\n\nInstall\n=======\n\n.. code-block:: bash\n\n    $ pip install meiz\n\nUsage\n=====\n\nYou can run ``mz download`` in one terminal, and run ``mz serve`` in\nanother terminal.\n\nThen open http://localhost:1310 in your browser.\n\n=========\n\n.. code-block:: bash\n\n    $ mz download --help\n    Usage: mz download [OPTIONS]\n\n      Download albums to ./images.\n\n    Options:\n      --max-workers INTEGER  The number of threads for downloading.  [default: 50]\n      --data-dir PATH        The directory to save albums.  [default: images]\n      --help                 Show this message and exit.\n\n\n.. code-block:: bash\n\n    $ mz serve --help\n    Usage: mz serve [OPTIONS]\n\n      Run a local http server.\n\n    Options:\n      --data-dir PATH  The directory to read albums.  [default: images]\n      --port INTEGER   The port of the http server.  [default: 1310]\n      --help           Show this message and exit.\n\n',
    'author': 'Meng Xiangzhuo',
    'author_email': 'aumo@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
