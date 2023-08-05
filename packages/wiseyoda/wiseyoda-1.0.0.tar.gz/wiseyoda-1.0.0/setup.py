# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wise_yoda']

package_data = \
{'': ['*'], 'wise_yoda': ['data/*']}

install_requires = \
['marshmallow-dataclass>=8.5.10,<9.0.0']

entry_points = \
{'console_scripts': ['wiseyoda = wise_yoda.cli:main']}

setup_kwargs = {
    'name': 'wiseyoda',
    'version': '1.0.0',
    'description': 'Quote the wise and powerful master Yoda.',
    'long_description': '#\n\n<div align="center">\n  <img width="1072" alt="logo" src="https://user-images.githubusercontent.com/1636709/210475936-9943ee5d-6bec-488d-a309-7a0df2312291.png">\n  <h1>WiseYoda</h1>\n\n  <p>\n    Quotes from the <a href="https://github.com/Mikaayenson/WiseYoda">Wise Yoda</a>\n  </p>\n\n\n<!-- Badges -->\n\n[![Supported Python versions](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)\n[![Python Testing](https://github.com/Mikaayenson/WiseYoda/actions/workflows/python-testing.yml/badge.svg)](https://github.com/Mikaayenson/WiseYoda/actions/workflows/python-testing.yml)\n\n<h5>\n    <a href="https://github.com/Mikaayenson/WiseYoda/issues/">Report Bug</a>\n  <span> · </span>\n    <a href="https://github.com/Mikaayenson/WiseYoda/issues/">Request Feature</a>\n  </h5>\n</div>\n\n<br />\n\n<!-- About the Project -->\n## :star2: About the Project\n\nSimple library to obtain wisdom from the wise Master Yoda in the form of quotes. Create a [feature request](https://github.com/Mikaayenson/WiseYoda/issues) if there are some useful features/commands that you hate to remember!\n\n<!-- Screenshots -->\n### :camera: Screenshots\n\n<p align="center">\n<img width="710" alt="Help" src="https://user-images.githubusercontent.com/1636709/210474079-0fd9c801-d6ba-4c87-8244-41a4c4ba5ed1.png">\n<img width="710" alt="Simple" src="https://user-images.githubusercontent.com/1636709/210474075-5ad35761-5765-49e7-ae22-62ff4aec85e1.png">\n<img width="710" alt="Complex" src="https://user-images.githubusercontent.com/1636709/210474078-d8c3c528-9bc6-4934-a970-4d372e3202a1.png">\n\n</p>\n\n<!-- Getting Started -->\n## :toolbox: Getting Started\n\n<!-- Prerequisites -->\n### :bangbang: Prerequisites\n\nThis project uses poetry as the python package manager\n\n- `poetry` Follow the [poetry install](https://python-poetry.org/docs/) guide\n- `python3.8+` Download from [python](https://www.python.org/downloads/) (ideally `3.10`)\n\n```bash\n   pip install wiseyoda\n```\n\n<!-- Usage -->\n## :eyes: Usage\n\nReminder: These commands must be run in the virtualenv where you installed the dependencies.\n\n```bash\n  from wise_yoda import Quotes\n  lesson = Quotes().random_quote()\n  lesson = Quotes().select_quote(season=1, episode=1)\n```\n\n<!-- Run Locally -->\n### :running: Run Locally\n\nClone the project\n\n```bash\n  git clone https://github.com/Mikaayenson/WiseYoda.git\n```\n\nGo to the project directory\n\n```bash\n  cd wise_yoda\n```\n\nInstall system and Python dependencies\n\n```bash\n  make deps\n```\n\nRun wiseyoda\n\n```bash\n  wiseyoda --help\n```\n\n<!-- Development -->\n### :construction: Development\n\n\n<div align="center">\n  <img width="710" alt="makefile" src="https://user-images.githubusercontent.com/1636709/210474182-474a778f-9267-4e7c-84d3-3edb48cc9f8a.png">\n</div>\n\nInstall pre-commit\n\n```bash\n  pre-commit install\n```\n\nUpdate Python dependencies\n\n```bash\n  make deps-py-update\n```\n\n<!-- Running Tests -->\n### :test_tube: Running Tests\n\nRun tests\n\n```bash\n  make test\n```\n\nRun linter\n\n```bash\n  make check\n```\n\n<!-- Build: Poetry -->\n### :triangular_flag_on_post: Build: Python Package\n\nBuild this project as a `sdist` and `wheel`\n\n```bash\n  make build\n```\n\n\n<!-- License -->\n## :warning: License\n\nDistributed under the Apache2.0 License. See LICENSE.txt for more information.\n',
    'author': 'Mika Ayenson',
    'author_email': 'Mika.ayenson@elastic.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Mikaayenson/WiseYoda',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
