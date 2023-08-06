# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bgetlib']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<2.26.0']

setup_kwargs = {
    'name': 'bgetlib',
    'version': '3.2.8',
    'description': 'A BiliBili API library',
    'long_description': '# bgetlib\n<a href="https://bgetlib.docs.josephcz.xyz/">\n    <img alt="Documentation" src="https://img.shields.io/badge/Documentation-66ccff">\n</a>\n<a href="https://github.com/baobao1270/bgetlib/blob/master/CHANGELOG">\n    <img alt="Changelog" src="https://img.shields.io/badge/Changelog-ee0000">\n</a>\n<a href="https://pypi.org/project/bgetlib/#history">\n    <img alt="Version" src="https://img.shields.io/pypi/v/bgetlib"></a>\n<a href="https://github.com/baobao1270/bgetlib/issues">\n    <img alt="Issues" src="https://img.shields.io/github/issues/baobao1270/bgetlib"></a>\n<a href="https://github.com/baobao1270/bgetlib/blob/master/LICENSE">\n    <img alt="License" src="https://img.shields.io/github/license/baobao1270/bgetlib">\n</a>\n\n**bgetlib** is a bilibili API library.\n\n## Install\n```shell\npip install bgetlib\n```\n\n## Quickstart\n```python\nimport bgetlib\nfrom bgetlib.models import QualityOptions\n\nbapi = bgetlib.BilibiliAPI("bilibili.com_cookies.txt")\n# https://space.bilibili.com/36081646/favlist?fid=976082846\nvideos = bapi.get_favorites_all(976082846)\nquality = QualityOptions()\n\nfor video in videos:\n    video_detail = bapi.get_video(video["id"])\n    for part in video_detail["pages"]:\n        bapi.save_stream(video_detail["aid"], part["cid"], quality, f"av{video[\'id\']}-P{part[\'page\']}.mp4")\n```\n',
    'author': 'Joseph Chris',
    'author_email': 'joseph@josephcz.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bgetlib.docs.josephcz.xyz/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
