# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['anki_export']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'anki-export',
    'version': '0.1.0',
    'description': 'Export your Anki *.apkg to Python. Read Anki *.apkg in Python.',
    'long_description': "# anki-export\n\nExport your Anki \\*.apkg to Python. Read Anki \\*.apkg in Python.\n\n## Example\n\n```python\nfrom anki_export import ApkgReader\nimport pyexcel_xlsxwx\n\nwith ApkgReader('test.apkg') as apkg:\n    pyexcel_xlsxwx.save_data('test.xlsx', apkg.export(), config={'format': None})\n```\n\n## Installation\n\n```commandline\n$ pip install anki-export\n```\n\n## Why?\n\n- \\*.apkg is quite well structured, convincing me to use this format more.\n- Allow you to use \\*.apkg programmatically in Python.\n- Might be less buggy than https://github.com/patarapolw/AnkiTools\n",
    'author': 'patarapolw',
    'author_email': 'patarapolw@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
