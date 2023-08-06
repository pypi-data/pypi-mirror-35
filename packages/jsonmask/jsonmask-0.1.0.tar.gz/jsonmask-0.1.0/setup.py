# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['jsonmask', 'jsonmask.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jsonmask',
    'version': '0.1.0',
    'description': 'Implements the Google Partial Response protocol in Python',
    'long_description': "Unix: [![Unix Build Status](https://img.shields.io/travis/craiglabenz/jsonmask/master.svg)](https://travis-ci.org/craiglabenz/jsonmask) Windows: [![Windows Build Status](https://img.shields.io/appveyor/ci/craiglabenz/jsonmask/master.svg)](https://ci.appveyor.com/project/craiglabenz/jsonmask)<br>Metrics: [![Coverage Status](https://img.shields.io/coveralls/craiglabenz/jsonmask/master.svg)](https://coveralls.io/r/craiglabenz/jsonmask) [![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/craiglabenz/jsonmask.svg)](https://scrutinizer-ci.com/g/craiglabenz/jsonmask/?branch=master)<br>Usage: [![PyPI Version](https://img.shields.io/pypi/v/jsonmask.svg)](https://pypi.org/project/jsonmask)\n\n# Overview\n\nImplements [Google Partial Response](https://developers.google.com/discovery/v1/performance#partial-response) / [`json-mask`](https://github.com/nemtsov/json-mask) in Python.\n\n## Requirements\n\n* Python 2.7\n* Python 3.6+\n\n## Installation\n\nInstall jsonmask with pip:\n\n```sh\n$ pip install jsonmask\n```\n\nor directly from the source code:\n\n```sh\n$ git clone https://github.com/zapier/jsonmask.git\n$ cd jsonmask\n$ python setup.py install\n```\n\n# Usage\n\nAfter installation, the package can imported:\n\n```sh\n$ python\n>>> import jsonmask\n>>> jsonmask.__version__\n```\n\nTo prune dictionaries:\n\n```py\nimport jsonmask\nmask = jsonmask.parse_fields('a,b(c,d)')\njsonmask.apply_json_mask(\n    {\n        'a': {\n            'nested_within_a': True,\n        },\n        'b' {\n            'c': True,\n            'd': {'Will get included?': 'Yes'},\n            'e': 'Tough luck here',\n        },\n        'c': 'Definitely hopeless',\n    },\n    mask,\n)\n\n>>> {\n        'a': {\n            'nested_within_a': True,\n        },\n        'b' {\n            'c': True,\n            'd': {'Will get included?': 'Yes'},\n        },\n    },\n```\n",
    'author': 'Craig Labenz',
    'author_email': 'craig.labenz@gmail.com',
    'url': 'https://github.com/zapier/jsonmask',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
}


setup(**setup_kwargs)
