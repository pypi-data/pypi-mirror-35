# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pyxtermjs']

package_data = \
{'': ['*']}

install_requires = \
['flask-socketio>=3.0,<4.0']

entry_points = \
{'console_scripts': ['pyxtermjs = pyxtermjs.app:main']}

setup_kwargs = {
    'name': 'pyxtermjs',
    'version': '0.1.0',
    'description': 'interactive terminal in the browser',
    'long_description': "# pyxterm.js\nA fully functional terminal in your browser.\n\n![screenshot](https://github.com/cs01/pyxterm.js/raw/master/pyxtermjs.png)\n\nThis is a Flask/socket.io websocket backend combined with the Xterm.js Javascript terminal emulator frontend. It works out of the box.\n\n## Installation\n\n### Option 1\nThis option installs system-wide or to your virtual environment. Should probably only be used if you're using a virtual environment.\n```\npip install pyxtermjs\npyxtermjs  # run it from anywhere\n```\n\n### Option 2\nThis option installs system-wide and isolates all of pyxterm.js's dependencies, guaranteeing there are no dependency version conflicts.\n```\npipsi install pyxtermjs\npyxtermjs  # run it from anywhere\n```\n\n### Option 3\nThis option lets you play around with the source code. Requires [poetry](https://github.com/sdispater/poetry) to be installed.\n```\ngit clone https://github.com/cs01/pyxterm.js.git\ncd pyxterm.js\npoetry install\npython pyxtermjs/app.py\n```\n",
    'author': 'Chad Smith',
    'author_email': 'cs01@users.noreply.github.com',
    'url': 'https://github.com/cs01/pyxterm.js',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
