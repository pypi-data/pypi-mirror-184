# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcane']

package_data = \
{'': ['*']}

install_requires = \
['mailjet_rest>=1.3.0,<2.0.0', 'typing-extensions>=3.7']

setup_kwargs = {
    'name': 'arcane-mailer',
    'version': '0.2.1',
    'description': 'Mail sender',
    'long_description': '# Arcane mailer\n\nThis package helps us to send mails',
    'author': 'Arcane',
    'author_email': 'product@arcane.run',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
