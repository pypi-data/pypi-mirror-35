# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['mirror_dict']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mirror-dict',
    'version': '1.0.0',
    'description': 'A mapping that returns the key if no value is found.',
    'long_description': '',
    'author': 'Jacob Hayes',
    'author_email': 'jacob.r.hayes@gmail.com',
    'url': 'https://github.com/JacobHayes/pymiscuous/tree/master/mirror-dict',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
