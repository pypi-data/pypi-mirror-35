# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['wemake_python_styleguide',
 'wemake_python_styleguide.logics',
 'wemake_python_styleguide.options',
 'wemake_python_styleguide.visitors',
 'wemake_python_styleguide.visitors.base']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.5,<4.0']

entry_points = \
{'flake8.extension': ['Z = wemake_python_styleguide.checker:Checker']}

setup_kwargs = {
    'name': 'wemake-python-styleguide',
    'version': '0.0.6',
    'description': 'Opinionated styleguide that we use in wemake.services',
    'long_description': '# wemake-python-styleguide\n\n[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)\n[![Build Status](https://travis-ci.org/wemake-services/wemake-python-styleguide.svg?branch=master)](https://travis-ci.org/wemake-services/wemake-python-styleguide)\n[![Coverage](https://coveralls.io/repos/github/wemake-services/wemake-python-styleguide/badge.svg?branch=master)](https://coveralls.io/github/wemake-services/wemake-python-styleguide?branch=master)\n[![PyPI version](https://badge.fury.io/py/wemake-python-styleguide.svg)](https://badge.fury.io/py/wemake-python-styleguide)\n[![Documentation Status](https://readthedocs.org/projects/wemake-python-styleguide/badge/?version=latest)](https://wemake-python-styleguide.readthedocs.io/en/latest/?badge=latest)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/wemake-services/wemake-python-styleguide/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n\nWelcome to the most opinionated linter ever.\n\n`wemake-python-styleguide` is actually just a `flake8` plugin.\nThe main goal of this tool is to make our `python` code consistent.\n\n\n## Installation\n\n```bash\npip install wemake-python-styleguide\n```\n\n## Project status\n\nWe are in early alpha. Use it on your own risk.\n\n\n## Contributing\n\nSee [`CONTRIBUTING.md`](/CONTRIBUTING.md) file if you want to contribute.\nYou can also check which [issues need some help](https://github.com/wemake-services/wemake-python-styleguide/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) right now.\n\n\n## License\n\nMIT. See [LICENSE.md](/LICENSE.md) for more details.\n',
    'author': 'Nikita Sobolev',
    'author_email': 'mail@sobolevn.me',
    'url': 'https://github.com/wemake-services/wemake-python-styleguide',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
