# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vnpy_sinopac', 'vnpy_sinopac.gateway']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.1,<2.0.0', 'shioaji>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'vnpy-sinopac',
    'version': '2.0.0',
    'description': 'The best trading API - Shioaji gateway with VNPY.',
    'long_description': '[![GitHub license](https://img.shields.io/github/license/ypochien/vnpy_sinopac)](https://github.com/ypochien/vnpy_sinopac/blob/main/LICENSE)\n[![GitHub issues](https://img.shields.io/github/issues/ypochien/vnpy_sinopac?style=plastic)](https://github.com/ypochien/vnpy_sinopac/issues)\n![GitHub Workflow Status (event)](https://img.shields.io/github/workflow/status/ypochien/vnpy_sinopac/Deploy?event=push)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vnpy_sinopac)\n![PyPI](https://img.shields.io/pypi/v/vnpy_sinopac)\n\n# Sinopac API - Shioaji 交易接口 for VeighNa框架\n\n# ⚠️ Warning ⚠️\n* ⚠️ 如果你的 shioaji 為 0.x 版本，請安裝 vnpy_sinopac v1.5\n* ⚠️ 如果你的 shioaji 為 1.0 版本之後，請安裝 vnpy_sinopac v2.0 之後的版本\n```\nimport shioaji\nprint(shioaji.__version__)\n```\n\n\n## \n- Sinopac API - shioaji - https://sinotrade.github.io/\n- VeighNa (VNPY) - https://github.com/vnpy/vnpy/\n- vnpy_sinopac - https://github.com/ypochien/vnpy_sinopac\n\n## Requirement\n* Shioaji >= 1.0\n* VeighNa 3.0~3.5\n* Python 3.10 / 3.9 / 3.8 / 3.7  (建議用 Anaconda)\n## Installation\n```\npip install vnpy_sinopac\n```\n## Quickstarts\n```\npython scripy/run.py\n```\nor add below\n```\nfrom vnpy_sinopac import SinopacGateway\n\nmain_engine.add_gateway(SinopacGateway)\n```\n\n\n## 關於下單方式\n### 股票\n\n\n### 期權\n\n\n\n## 贊助 Donating\n* 如果你發現這個專案有幫助到你，請考慮 [贊助](https://etherscan.io/address/ypochien.eth)\n* ETH是最棒的，但其他TOKEN也都歡迎。\n* ![ypochien.eth.png](ypochien.eth.png)\n\n\n\n',
    'author': 'ypochien',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ypochien/vnpy_sinopac',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
