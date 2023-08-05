# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magneto_pyelastica']

package_data = \
{'': ['*']}

install_requires = \
['pyelastica @ git+https://github.com/GazzolaLab/PyElastica.git@update-0.3.0']

extras_require = \
{'examples': ['cma[examples]>=3.2.2,<4.0.0']}

setup_kwargs = {
    'name': 'magneto-pyelastica',
    'version': '0.0.1',
    'description': 'Python software for simulating magnetic Cosserat rods.',
    'long_description': None,
    'author': 'Arman Tekinalp',
    'author_email': 'armant2@illinois.edu>, Yashraj Bhosale <bhosale2@illinois.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/armantekinalp/MagnetoPyElastica',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
