# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['okadminfinder', 'okadminfinder.LinkFile']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0',
 'colorama>=0.4.6,<0.5.0',
 'httpx[socks]>=0.23.1,<0.24.0',
 'tqdm>=4.64.1,<5.0.0',
 'trio>=0.22.0,<0.23.0']

entry_points = \
{'console_scripts': ['okadminfinder = okadminfinder.okadminfinder:main']}

setup_kwargs = {
    'name': 'okadminfinder',
    'version': '1.0.0',
    'description': '[ Admin panel finder / Admin Login Page Finder ] ¢σ∂є∂ ву 👻 (❤-❤) 👻',
    'long_description': '![](https://gist.githubusercontent.com/mIcHyAmRaNe/0b370c808bd1a600778f6a3875e5a732/raw/35f2803c176eeb27d4eea5eac88087b0d78f0ecc/okadminfinder3-.png)\n\n[![Build Status](https://travis-ci.org/mIcHyAmRaNe/okadminfinder3.svg?branch=master)](https://travis-ci.org/mIcHyAmRaNe/okadminfinder)\n[![GitHub license](https://img.shields.io/github/license/mIcHyAmRaNe/okadminfinder3.svg)](https://github.com/mIcHyAmRaNe/okadminfinder/blob/master/LICENSE)\n![](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20osx-lightgrey.svg)\n[![GitHub stars](https://img.shields.io/github/stars/mIcHyAmRaNe/okadminfinder3.svg?style=social)](https://github.com/mIcHyAmRaNe/okadminfinder/stargazers)\n[![Downloads](https://pepy.tech/badge/okadminfinder/week)](https://pepy.tech/project/okadminfinder)\n[![Downloads](https://pepy.tech/badge/okadminfinder)](https://pepy.tech/project/okadminfinder)\n\n## OKadminFinder: Easy way to find admin panel of website\n\n*OKadminFinder is an Apache2 Licensed utility, rewritten in **Python 3.x**, for admins/pentesters who want to find admin panel of a website. There are many other tools but not as effective and secure. Yeah, Okadminfinder has the the ability to use tor and hide your identity*\n\n* ## Requirements\n    ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)\n    ![PyPI](https://img.shields.io/pypi/v/argparse.svg?label=argparse)\n    ![PyPI](https://img.shields.io/pypi/v/colorama.svg?label=colorama)\n    ![PyPI](https://img.shields.io/pypi/v/httpx.svg?label=httpx)\n    ![PyPI](https://img.shields.io/pypi/v/trio.svg?label=trio)\n    ![PyPI](https://img.shields.io/pypi/v/tqdm.svg?label=tqdm)\n    * #### Linux\n       ```bash\n       ❯ sudo apt install tor\n       ❯ sudo service tor start\n       ```\n\n    * #### Windows\n       download [tor windows expert bundle](https://www.torproject.org/download/tor/)\n\n* ## Preview\n   <a href="http://www.youtube.com/watch?feature=player_embedded&v=5C9aOinwKAs" target="_blank">\n      <img src="https://i.imgur.com/610tOPC.png" alt="Watch the video" border="10" />\n   </a>\n\n* ## Installation\n      \n   * #### PyPi\n      ```bash\n      # Install\n      ❯ pip install okadminfinder\n      # Update\n      ❯ pip install --upgrade okadminfinder\n      # Remove\n      ❯ pip uninstall okadminfinder\n\n\n      # Usage\n      ❯ okadminfinder -h\n      ```\n   \n   * #### Git Clone\n      ```bash\n      # Download and Usage\n      ❯ git clone https://github.com/mIcHyAmRaNe/okadminfinder3.git\n      ❯ cd okadminfinder3\n      ❯ chmod +x okadminfinder.py\n      ❯ ./okadminfinder.py -h\n      ```\n\n## Features\n- [x] Multiplatforms `(Windows/Linux/MacOS)`\n- [x] Easy to install, update and even remove\n- [x] More than 1000 potential admin panels\n- [x] Console works with params, like: `❯ okadminfinder -u https://example.com --proxy 127.0.0.1:8080`\n- [x] Random-Agents\n- [x] HTTP/HTTPS Proxies\n- [x] Socks4/5 & Tor\n\n## Youtube videos\n- [okadminfinder : PyPi version](https://youtu.be/5C9aOinwKAs/)\n- [okadminfinder : admin page finder](https://youtu.be/DluCL4aA9UU/)\n- [okadminfinder3 : admin page finder (update)](https://youtu.be/iJg4NJT5qkY/)\n- [admin panel finder Kali Linux 2018.3](https://youtu.be/kY9KeDqY5QQ)\n\n## Most Blogs that shared okadminfinder\n- [kitploit.com](https://www.kitploit.com/2019/04/okadminfinder3-admin-panel-finder-admin.html)\n- [securityonline.info](https://securityonline.info/admin-login-page-finder/)\n- [prodefence.org](https://www.prodefence.org/okadminfinder3-admin-login-page-finder/)\n- [kalilinuxtutorials.com](https://kalilinuxtutorials.com/okadminfinder-admin-panel/)\n- [onehack.us](https://onehack.us/t/how-to-find-website-admin-panel-using-okadminfinder-tool-easy-method/64840)\n- [the-realworld.org](https://the-realworld.org/okadminfinder-finder-du-panneau-dadministration-finder-admin-page-finder)\n- [crackitdown.com](https://www.crackitdown.com/2019/12/find-admin-panel-using-OkadminFinder.html)\n- [securitynewspaper.com](https://www.securitynewspaper.com/2020/01/02/find-hidden-admin-page-of-any-website/)\n',
    'author': 'mIcHyAmRaNe',
    'author_email': 'marseillaisanonymous@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://michyamrane.github.io/tools/okadminfinder/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
