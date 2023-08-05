# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imgextractor']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'numpy>=1.23.5,<2.0.0',
 'tensorflow-hub>=0.12.0,<0.13.0',
 'tensorflow>=2.11.0,<3.0.0',
 'tflite-support>=0.4.3,<0.5.0']

entry_points = \
{'console_scripts': ['imgextract = imgextract:main.main']}

setup_kwargs = {
    'name': 'imgextractor',
    'version': '0.1.1',
    'description': 'Extract images from images',
    'long_description': '',
    'author': 'Jiri Podivin',
    'author_email': 'jpodivin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
