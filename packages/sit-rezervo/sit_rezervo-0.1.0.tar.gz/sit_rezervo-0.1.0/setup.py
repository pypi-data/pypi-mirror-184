# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sit_rezervo', 'sit_rezervo.notify', 'sit_rezervo.utils']

package_data = \
{'': ['*']}

install_requires = \
['dataclass-wizard[yaml]>=0.22.2,<0.23.0',
 'fastapi>=0.88.0,<0.89.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'pytz>=2022.7,<2023.0',
 'requests>=2.28.1,<3.0.0',
 'slack-sdk>=3.19.5,<4.0.0',
 'typer>=0.7.0,<0.8.0',
 'uvicorn>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['sit-rezervo = sit_rezervo.cli:cli']}

setup_kwargs = {
    'name': 'sit-rezervo',
    'version': '0.1.0',
    'description': 'Automatic booking of Sit Trening group classes',
    'long_description': '# sit-rezervo\n\n[![PyPI](https://img.shields.io/pypi/v/sit-rezervo)](https://pypi.org/project/sit-rezervo/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sit-rezervo)\n\nAutomatic booking of [Sit Trening group classes](https://www.sit.no/trening/gruppe)',
    'author': 'Mathias Oterhals Myklebust',
    'author_email': 'mathias@oterbust.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mathiazom/sit-rezervo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
