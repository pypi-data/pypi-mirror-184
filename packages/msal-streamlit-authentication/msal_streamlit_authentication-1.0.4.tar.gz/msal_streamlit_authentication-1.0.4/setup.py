# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['msal_streamlit_authentication']

package_data = \
{'': ['*'],
 'msal_streamlit_authentication': ['frontend/dist/*', 'frontend/dist/assets/*']}

install_requires = \
['streamlit']

setup_kwargs = {
    'name': 'msal-streamlit-authentication',
    'version': '1.0.4',
    'description': 'Streamlit Authentication library based on MSAL.JS',
    'long_description': 'Streamlit Authentication library based on MSAL.JS',
    'author': 'Michael Staal-Olsen',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mstaal/msal_streamlit_authentication',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.12,<3.12',
}


setup(**setup_kwargs)
