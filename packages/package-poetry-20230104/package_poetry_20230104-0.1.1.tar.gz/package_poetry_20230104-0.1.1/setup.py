# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pacpoetry']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'jupyter>=1.0.0,<2.0.0', 'pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'package-poetry-20230104',
    'version': '0.1.1',
    'description': 'This is a package publication test from Poetry',
    'long_description': 'My long description blah blah blah blah.\nChange Log\n================\n0.0.1 (Dec 1, 2021)\n — — — — — — — — — — — — — — — -\n- First Release\n0.0.2 (Dec 2, 2021)\n — — — — — — — — — — — — — — — -\n- Did some more stuff',
    'author': 'Arthur Couget',
    'author_email': 'arthur.couget@viseo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DjKuj/package-poetry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
