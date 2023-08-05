# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['horology']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'horology',
    'version': '1.3.1',
    'description': 'Conveniently measures the time of loops, contexts and functions.',
    'long_description': '# `Horology`\n\n[![PyPI version](https://badge.fury.io/py/horology.svg)](https://badge.fury.io/py/horology)\n[![tests](https://github.com/mjmikulski/horology/actions/workflows/tests.yaml/badge.svg)](https://github.com/mjmikulski/horology/actions/workflows/tests.yaml)\n[![codeql](https://github.com/mjmikulski/horology/actions/workflows/codeql.yaml/badge.svg)](https://github.com/mjmikulski/horology/actions/workflows/codeql.yaml)\n[![PythonVersion](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://pypi.org/project/horology/)\n[![PythonVersion](https://img.shields.io/badge/OS-linux%20%7C%20windows%20%7C%20macos-green)](https://pypi.org/project/horology/)\n[![Downloads](https://pepy.tech/badge/horology/month)](https://pepy.tech/project/horology)\n\nConveniently measures the time of your loops, contexts and functions.\n\n![](hourglass.jpg "Photo by Mike from Pexels")\n\n## Installation\n\n| horology version | compatible python |\n|------------------|-------------------|\n| 1.3              | 3.8-3.11          |\n| 1.2              | 3.6-3.9           |\n| 1.1              | 3.6-3.8           |\n\nHorology can be installed with PIP. It has no dependencies.\n\n```\npip install horology\n```\n\n## Usage\n\nThe following 3 tools will let you measure practically any part of your Python code.\n\n### Timing an iterable (list, tuple, generator, etc)\n\n#### Quick example\n\n```python\nfrom horology import Timed\n\nanimals = [\'cat\', \'dog\', \'crocodile\']\n\nfor x in Timed(animals):\n    feed(x)\n```\n\nResult:\n\n```\niteration    1: 12.0 s\niteration    2: 8.00 s\niteration    3: 100 s\n\ntotal 3 iterations in 120 s\nmin/median/max: 8.00/12.0/100 s\naverage (std): 40.0 (52.0) s\n\n```\n\n#### Customization\n\nYou can specify where (if at all) you want each iteration and summary to be printed, eg.:\n\n```python\nfor x in Timed(animals, unit=\'ms\',\n               iteration_print_fn=logger.debug,\n               summary_print_fn=logger.info):\n    feed(x)\n```\n\n### Timing a function with a `@timed` decorator\n\n#### Quick example\n\n```python\nfrom horology import timed\n\n\n@timed\ndef foo():\n    ...\n```\n\nResult:\n\n```\n>>> foo()\nfoo: 7.12 ms\n```\n\n#### Customization\n\nChose time unit and name:\n\n```python\n@timed(unit=\'s\', name=\'Processing took \')\ndef bar():\n    ...\n```\n\nResult:\n\n```\n>>> bar()\nProcessing took 0.185 s\n```\n\n### Timing part of code with a `Timing` context\n\n#### Quick example\n\nJust wrap your code using a `with` statement\n\n```python\nfrom horology import Timing\n\nwith Timing(name=\'Important calculations: \'):\n    ...\n```\n\nResult:\n\n```\nImportant calculations: 12.4 s\n```\n\n#### Customization\n\nYou can suppress default printing and directly use measured time (also within context)\n\n```python\nwith Timing(print_fn=None) as t:\n    ...\n\nmake_use_of(t.interval)\n```\n\n## Time units\n\nTime units are by default automatically adjusted, for example you will see\n`foo: 7.12 ms` rather than `foo: 0.007 s`. If you don\'t like it, you can\noverride this by setting the `unit` argument with one of these names:\n`[\'ns\', \'us\', \'ms\', \'s\', \'min\', \'h\', \'d\']`.\n\n## Contributions\n\nContributions are welcomed, see [contribution guide](.github/contributing.md).\n\n## Internals\n\nHorology internally measures time with `perf_counter` which provides the *highest available resolution,*\nsee [docs](https://docs.python.org/3/library/time.html#time.perf_counter).\n',
    'author': 'mjmikulski',
    'author_email': 'maciej.mikulski.jr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mjmikulski/horology',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
