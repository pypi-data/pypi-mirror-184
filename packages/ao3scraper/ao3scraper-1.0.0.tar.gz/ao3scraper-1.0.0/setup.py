# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ao3scraper', 'ao3scraper.tests']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0',
 'Pygments==2.12.0',
 'SQLAlchemy>=1.4.41,<2.0.0',
 'alembic>=1.8.1,<2.0.0',
 'ao3-api>=2.3.0,<3.0.0',
 'beautifulsoup4==4.11.1',
 'certifi==2022.5.18.1',
 'chardet==4.0.0',
 'click==8.0.1',
 'commonmark==0.9.1',
 'configparser>=5.3.0,<6.0.0',
 'deepdiff[murmur]>=5.8.1,<6.0.0',
 'dictdiffer>=0.9.0,<0.10.0',
 'idna==2.10',
 'marshmallow-sqlalchemy>=0.28.1,<0.29.0',
 'pathlib>=1.0.1,<2.0.0',
 'platformdirs>=2.5.4,<3.0.0',
 'requests==2.25.1',
 'rich==12.4.1',
 'ruamel-yaml>=0.17.21,<0.18.0',
 'soupsieve==2.3.2.post1',
 'urllib3==1.26.9']

setup_kwargs = {
    'name': 'ao3scraper',
    'version': '1.0.0',
    'description': '',
    'long_description': 'None',
    'author': 'Ethan',
    'author_email': 'ethanjohnleitch@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
