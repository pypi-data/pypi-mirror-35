# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['monospace',
 'monospace.core',
 'monospace.core.domain',
 'monospace.core.formatting',
 'monospace.core.rendering',
 'monospace.core.symbols']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7,<7.0',
 'ptpython==0.41.0',
 'pypandoc>=1.4,<2.0',
 'pyphen>=0.9.5,<0.10.0']

setup_kwargs = {
    'name': 'monospace',
    'version': '0.1.1',
    'description': 'Book typesetter for the terminal',
    'long_description': '<pre>\n\n\n\n                                ┌─────┬───┬───┬───┬───┬───┬───┬───┬───┐\n                                │ ╷ ╷ │ · │ ╷ │ · ├   ┤ · │ · │   ┤   ╡\n                                └─┴─┴─┴───┴─┴─┴───┴───┤ ┌─┴─┴─┴───┴───┘\n                                                      └─┘\n                                     <i>A fixed-width book typesetter</i>\n\n                         Now re-implementing from scratch, powered by <a href="https://pandoc.org/">ᴘᴀɴᴅᴏᴄ</a>.\n\n\n   ━━━━━━━━━━━━━━━━━━\n      <b>About monospace</b>    While this readme is incomplete, you can read about the concept\n                         for the project in the <a href="poc/README.md">ᴏʟᴅ ʀᴇᴀᴅᴍᴇ</a>. \n              <i>A short</i>    \n         <i>introduction</i>    Or maybe you can get a preview of what is to come¹ with some\n                         mockups of the current rendering target:\n             ¹: Soon™\n                         <img width="520" alt="page1" src="https://user-images.githubusercontent.com/4116708/44863793-64b15480-ac7e-11e8-9957-3f760c9b0e74.png">\n\n                                       <i>Figure 1: first page of the mockup</i>\n\n\n                         <img width="520" alt="page2" src="https://user-images.githubusercontent.com/4116708/44863794-64b15480-ac7e-11e8-91d3-36a17805270a.png">\n\n                                      <i>Figure 2: second page of the mockup</i>\n\n\n</pre>',
    'author': 'Hamza Haiken',
    'author_email': 'tenchi@team2xh.net',
    'url': 'https://github.com/Tenchi2xh/monospace',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
