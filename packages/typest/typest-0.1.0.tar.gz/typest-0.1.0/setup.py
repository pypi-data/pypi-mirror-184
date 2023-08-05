# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typest', 'typest.utils']

package_data = \
{'': ['*']}

install_requires = \
['comment-parser>=1.2.4,<2.0.0', 'mypy>=0.991,<0.992']

setup_kwargs = {
    'name': 'typest',
    'version': '0.1.0',
    'description': 'A framework for testing type expectations',
    'long_description': '# typest\n\nFramework to test your library against type checkers, allowing to create\nexpected errors and. Its purpose is the same as the one of\n[pytest-mypy-plugins](https://pypi.org/project/pytest-mypy-plugins/). While\n`pytest-mypy-plugins` requires `.yaml` files for specifying the tests,\n`typest` test cases are python files, expectations are formulated in comments:\n\n```Python\nfrom mylibrary import some_function\n\nresult = some_function()\n\nreveal_type(result)  # expect-type: int\n```\n\nBesides expressing type expectations, you can also specify to expect an error\nfrom the typechecker:\n\n```Python\nstring: str = "not a number"\nnumber: int = string  # expect-error\n```\n\nYou can also specify which error you expect:\n\n```Python\nstring: str = "not a number"\nnumber: int = string  # expect-error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]\n```\n',
    'author': 'Jonathan Scholbach',
    'author_email': 'j.scholbach@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
