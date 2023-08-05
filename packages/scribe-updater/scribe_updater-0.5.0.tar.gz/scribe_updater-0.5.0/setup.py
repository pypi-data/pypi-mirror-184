# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['scribe_updater']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['updater = scribe_updater.console:main']}

setup_kwargs = {
    'name': 'scribe-updater',
    'version': '0.5.0',
    'description': 'A tool to upgrade scribe configuration files',
    'long_description': '#### Run\npoetry run updater\n\n#### Test\npoetry run pytest \n\n#### Coverage\npoetry run pytest --cov\n\n#### Caveats\nif you are getting an error that looks like this :<br> `Failed to create the collection: Prompt dismissed..`<br>\nthen export the following environment variable: <br>\n`export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring`',
    'author': 'Paul Cardoos',
    'author_email': 'paul.cardoos@clinc.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
