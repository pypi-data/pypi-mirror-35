# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['logconf']
setup_kwargs = {
    'name': 'logconf',
    'version': '0.1.0',
    'description': 'convenient python stdlib logging configuration',
    'long_description': None,
    'author': 'Andreas Lutro',
    'author_email': 'anlutro@gmail.com',
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
