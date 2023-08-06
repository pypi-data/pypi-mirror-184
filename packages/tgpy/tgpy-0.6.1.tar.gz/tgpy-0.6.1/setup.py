# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tgpy', 'tgpy.handlers', 'tgpy.run_code']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'aiorun>=2022.4.1,<2023.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'cryptg-anyos>=0.4.1,<0.5.0',
 'rich>=12.5.1,<13.0.0',
 'telethon-v1-24==1.24.4']

entry_points = \
{'console_scripts': ['tgpy = tgpy.main:main']}

setup_kwargs = {
    'name': 'tgpy',
    'version': '0.6.1',
    'description': 'Run Python code right in your Telegram messages',
    'long_description': '# TGPy\n\n[![PyPI](https://img.shields.io/pypi/v/tgpy)](https://pypi.org/project/tgpy/)\n[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/tgpy/tgpy?label=docker&sort=semver)](https://hub.docker.com/r/tgpy/tgpy)\n[![Open issues](https://img.shields.io/github/issues-raw/tm-a-t/TGPy)](https://github.com/tm-a-t/TGPy/issues)\n[![Docs](https://img.shields.io/website?label=docs&url=https%3A%2F%2Ftgpy.tmat.me)](https://tgpy.tmat.me/)\n<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/tgpy) -->\n\n**Run Python code right in your Telegram messages.** TGPy is a tool built on top of [Telethon](https://github.com/LonamiWebs/Telethon).\n\n- Calculate right in chats\n- Send messages, save files, analyze chats &mdash; with simple code\n- Set up functions to automate your Telegram actions\n\n[Basics Guide](http://tgpy.tmat.me/basics/code/) · [Extensibility Guide](http://tgpy.tmat.me/extensibility/context/) · [Reference](http://tgpy.tmat.me/reference/builtins/)\n\n## Getting started\n\nPython 3.9+ required. Install TGPy and connect it to your Telegram account:\n\n```shell\n> pip install tgpy\n> tgpy\n```\n\nYou’re ready now. Send Python code to any chat, and it will run. Change your message to change the result.\n\n[Details on installation](http://tgpy.tmat.me/installation/)\n\nhttps://user-images.githubusercontent.com/38432588/181266550-c4640ff1-71f2-4868-ab83-6ea3690c01b6.mp4\n\n## Inspiration\n\nTGPy is inspired by [FTG](https://gitlab.com/friendly-telegram/friendly-telegram) and similar userbots. However, the key concept is different: TGPy is totally based on usage of code in Telegram rather than plugging extra modules. This leads both to convenience of single-use scripts and reusage flexibility.\n\n## Credits\n\nTGPy is built on [Telethon](https://github.com/LonamiWebs/Telethon), which allows to integrate Telegram features in Python code.\n\nBasic code transformation (such as auto-return of values) is based on [meval](https://github.com/penn5/meval).\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'tmat',
    'author_email': 'a@tmat.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tm-a-t/TGPy/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
