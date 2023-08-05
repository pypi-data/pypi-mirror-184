# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lm_identifier']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1,<2.0.0', 'torch>=1.13.1,<2.0.0', 'transformers>=4.25.1,<5.0.0']

setup_kwargs = {
    'name': 'lm-identifier',
    'version': '0.0.1',
    'description': 'A toolkit for identifying pretrained language models from AI-generated text',
    'long_description': '# LM Identifier\n\nWith a surge of generative pretrained language models, it is becoming increasingly important to distinguish between human and AI-generated text. Inspired by [GPTZero](https://etedward-gptzero-main-zqgfwb.streamlit.app), an app that seeks to detect AI-generated text, LM Identifier pokes at this question even further by providing a growing suite of tools to help identify *which (publicly available) language model* might have been used to generate some given chunck of text.\n\n## Installation\n\nLM Identifier is available on PyPI.\n\n```\n$ pip install lm-identifier\n```\n\nTo develop locally, first install pre-commit:\n\n```\n$ pip install --upgrade pip wheel\n$ pip install pre-commit\n$ pre-commit install\n```\n\nInstall the package in editable mode.\n\n```\npip install -e .\n```\n\n## Usages\n\nWIP\n',
    'author': 'Jaesung Tae',
    'author_email': 'jaesungtae@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
