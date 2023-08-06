# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gc_integrations',
 'gc_integrations.config',
 'gc_integrations.hltb',
 'gc_integrations.igdb',
 'gc_integrations.igdb.models',
 'gc_integrations.igdb.utils',
 'gc_integrations.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'howlongtobeatpy>=1.0.5,<2.0.0',
 'httpx>=0.23.3,<0.24.0',
 'pydantic>=1.10.3,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'game-core-integrations',
    'version': '0.2.5',
    'description': 'The integrations library for GameCore.',
    'long_description': '# GameCore Integrations Library\n\nThis is the library responsible for GameCore integrations.  \nAsync code is used whenever possible, with synchronous code being "converted" and run in the main loop thread.\n\nWhile closely related to GameCore needs, this library can be used on it\'s own to support different services.  \nMost integrations are based on third-party open source libraries, so you may prefer to use these instead.\n\n- [GameCore Integrations Library](#gamecore-integrations-library)\n  - [Integrations](#integrations)\n\n\n## Integrations\n\nIntegrations are what power GameCore\'s search, playtime queries, user libraries, etc.\n\nWe have plans to support and integrate the following services:\n\n- [ ] IGDB  \nThis is our main search provider.\nDeveloped in-house.\n\n- [ ] HowLongToBeat  \nFor playtime related information.\n\n- [ ] Steam  \nIntegration for populating user libraries with Steam games and achievements.\n\n- [ ] PSN  \nIntegration for populating user libraries with PSN games and achievements.  \n\nPowered by the [psnawp](https://github.com/isFakeAccount/psnawp) Python library.\n\n- [ ] Xbox Live  \nIntegration for populating user libraries with Xbox Live games and achievements\n\n',
    'author': 'Lamarcke',
    'author_email': 'cassiolamarcksilvafreitas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
