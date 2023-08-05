# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['accumulate']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'accumulate',
    'version': '1.0.0',
    'description': 'Inheritance for iterable attributes.',
    'long_description': 'accumulate\n----------\n\nPackage `accumulate` eases inheritance of iterable class attributes by accumulating values along the MRO.\n',
    'author': 'Jacob Hayes',
    'author_email': 'jacob.r.hayes@gmail.com',
    'url': 'https://github.com/JacobHayes/pymiscuous/tree/master/accumulate',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
