# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdfpaper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pdfpaper',
    'version': '0.1.1',
    'description': 'pdf paper parser',
    'long_description': '# pdfpaper\n\npdf论文格式解析和信息提取\n\n',
    'author': 'luzhixing12345',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
