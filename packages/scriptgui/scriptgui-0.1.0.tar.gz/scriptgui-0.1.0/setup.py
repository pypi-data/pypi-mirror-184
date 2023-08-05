# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scriptgui']

package_data = \
{'': ['*']}

install_requires = \
['flask==2.0.1', 'idom[flask]>=0.42.0,<0.43.0', 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['ms = scriptgui.web:main']}

setup_kwargs = {
    'name': 'scriptgui',
    'version': '0.1.0',
    'description': 'organize and interact with scripts via a plugin style pattern, using a browser based interface',
    'long_description': 'None',
    'author': 'tyler jones',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
