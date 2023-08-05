# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['libaloha',
 'libaloha.bin',
 'libaloha.cache',
 'libaloha.django',
 'libaloha.markdown']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.19,<3.0']

extras_require = \
{'django': ['django==2.0.6'],
 'markdown': ['markdown>=2.6,<3.0'],
 'redis': ['redis>=2.10,<3.0']}

entry_points = \
{'console_scripts': ['check-ip = libaloha.bin:check_ip',
                     'check-website-alive = libaloha.bin:check_website_alive',
                     'send-sms = libaloha.bin:send_sms']}

setup_kwargs = {
    'name': 'libaloha',
    'version': '0.0.1',
    'description': 'Personal library to provide some classes, functions and binaries',
    'long_description': '# libaloha: Personal library to provide some classes, functions and binaries\n\nThis is just a little python package I use to centralize my dev works. Enjoy it if you want :-)\n\n## Modules\n\n### aloha.cache\n\n**aloha.cache.redis** need the **redis** package installed.\n\n### aloha.django\n\n**aloha.django** need the **django** package installed.\n\n### aloha.markdown\n\n**aloha.markdown** need the **markdown** package installed.\n',
    'author': 'Aloha68',
    'author_email': 'dev@aloha.im',
    'url': 'https://gitlab.com/aloha68/libaloha',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
