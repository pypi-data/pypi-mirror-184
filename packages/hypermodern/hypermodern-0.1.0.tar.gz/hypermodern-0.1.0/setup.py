# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hypermodern']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.45,<2.0.0',
 'cleo>=2.0.1,<3.0.0',
 'click>=8.0.4,<9.0.0',
 'csvkit>=1.0.7,<2.0.0',
 'desert>=2022.9.22,<2023.0.0',
 'httpx>=0.23.1,<0.24.0',
 'isort>=5.11.4,<6.0.0',
 'marshmallow>=3.19.0,<4.0.0',
 'mypy>=0.991,<0.992',
 'requests>=2.28.1,<3.0.0',
 'typer>=0.7.0,<0.8.0',
 'types-requests>=2.28.11.7,<3.0.0.0']

entry_points = \
{'console_scripts': ['wiki = hypermodern.console:main']}

setup_kwargs = {
    'name': 'hypermodern',
    'version': '0.1.0',
    'description': '',
    'long_description': '[![Tests](https://github.com/redcodeworks/hypermodern/workflows/Tests/badge.svg)](https://github.com/redcodeworks/hypermodern/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/redcodeworks/hypermodern/branch/main/graph/badge.svg)](https://codecov.io/gh/redcodeworks/hypermodern)\n[![PyPI](https://img.shields.io/pypi/v/hypermodern.svg)](https://pypi.org/project/hypermodern/)\n',
    'author': 'Kevin Riley',
    'author_email': 'kevin@redcode.works',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
