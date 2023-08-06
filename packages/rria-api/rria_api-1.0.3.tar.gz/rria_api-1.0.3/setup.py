# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rria_api', 'rria_api.gen3', 'rria_api.gen3.api_gen3', 'rria_api.ned']

package_data = \
{'': ['*']}

install_requires = \
['pyniryo>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'rria-api',
    'version': '1.0.3',
    'description': '',
    'long_description': "# RRIA-API\n\nThe `rria-api` is an easy-to-use package that provides a common interface to control robots used by the Residence in Robotics\nand AI at the UFPE's informatics center. The API currently supports the use of Kinova Gen3 lite and Niryo NED, with\nplans to support a Denso robot.\n\n### **Requirements**\n\n- Python 3.9+\n- Kortex API .whl package\n\n### **Instalation**\n1. Download the v2.3.0 Kortex API .whl package (required for controlling the Kinova Gen3 and Gen3 lite):\n\n- [kortex_api-2.3.0.post34-py3-none-any.whl](https://artifactory.kinovaapps.com/ui/native/generic-public/kortex/API/2.3.0/kortex_api-2.3.0.post34-py3-none-any.whl).\n\n2. Install the downloaded package with `pip`:\n\n```\n$ pip install <path to kortex_api-2.3.0.post34-py3-none-any.whl>\n```\n\n3. Install the latest `rria-api` package with `pip`:\n\n```\n$ pip install rria-api\n```",
    'author': 'felipeadsm',
    'author_email': '97059009+felipeadsm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
