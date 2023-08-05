# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zq_django_util',
 'zq_django_util.exceptions',
 'zq_django_util.logs',
 'zq_django_util.logs.migrations',
 'zq_django_util.response',
 'zq_django_util.utils',
 'zq_django_util.utils.auth',
 'zq_django_util.utils.oss',
 'zq_django_util.utils.user']

package_data = \
{'': ['*'], 'zq_django_util.logs': ['templates/*']}

install_requires = \
['djangorestframework-simplejwt>=4.7,<6.0',
 'drf-standardized-errors>=0.9.0,<0.13.0',
 'oss2>=2.13.0,<3.0']

setup_kwargs = {
    'name': 'zq-django-util',
    'version': '0.1.0',
    'description': '自强Studio Django 工具',
    'long_description': '# zq-django-util\n\n## 依赖兼容性\n\n### drf\n- 3.14: Python 3.6+, Django 4.1, 4.0, 3.2, 3.1, 3.0\n- 3.13: Python 3.6+, Django 4.0, 3.2, 3.1, 2.2\n- 3.12: Python 3.6+, Django 3.2, 3.1, 2.2\n\n### Django\n- 4.1: Python 3.8, 3.9, 3.10, and 3.11\n- 4.0: Python 3.8, 3.9, and 3.10\n- 3.2: Python 3.6, 3.7, 3.8, 3.9 and 3.10\n\n### oss2\n- Python 3.7+\n\n### drf-standardized-errors\n- 0.12.3: add support for python 3.11\n- 0.12.2: add support for DRF 3.14\n- 0.12.0: add support for django 4.1\n',
    'author': 'Nagico',
    'author_email': 'yjr888@vip.qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
