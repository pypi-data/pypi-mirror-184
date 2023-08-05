# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tamrof']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tamrof',
    'version': '0.0.0',
    'description': 'A fast, highly opinionated Python formatter',
    'long_description': '# tamrof\nA fast, highly opinionated Python formatter\n',
    'author': 'Isaac Harris-Holt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
