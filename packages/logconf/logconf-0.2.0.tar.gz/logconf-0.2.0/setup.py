# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['logconf']
setup_kwargs = {
    'name': 'logconf',
    'version': '0.2.0',
    'description': 'convenient python stdlib logging configuration',
    'long_description': '# logconf\n\n[![Build Status](https://travis-ci.org/anlutro/logconf.py.svg?branch=master)](https://travis-ci.org/anlutro/logconf.py)\n[![Latest version on PyPI](https://img.shields.io/pypi/v/logconf.svg?maxAge=2592000)](https://pypi.org/project/logconf)\n[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n\nSetting up logging in Python is verbose and error prone. This library aims to fix that, without replacing the standard library logging entirely.\n\n```python\nimport logging\nfrom logconf import logconf\n\nwith logconf() as logger:\n    # simple example:\n    logger.log_to_console_if_interactive(level=logging.DEBUG)\n    if os.getenv(\'LOG_DEST\'):  # can be "stdout" or "stderr"\n        logger.log_to_file(os.getenv(\'LOG_DEST\'), level=os.getenv(\'LOG_LEVEL\'))\n\n    # more fine-grained control:\n    logger.log_json_to_file(\'/var/log/myapp.jsonlog\', level=logging.WARNING)\n    logger.log_json_to_file(\'/var/log/myapp_debug.jsonlog\', level=logging.DEBUG)\n\n    # configure sub-loggers:\n    with logger.logger(\'urllib3\') as sublogger:\n        sublogger.level = logging.WARNING\n    with logger.logger(\'myapp.security\') as sublogger:\n        sublogger.log_to_file(\'/var/log/myapp.security.log\', level=logging.INFO)\n```\n',
    'author': 'Andreas Lutro',
    'author_email': 'anlutro@gmail.com',
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
