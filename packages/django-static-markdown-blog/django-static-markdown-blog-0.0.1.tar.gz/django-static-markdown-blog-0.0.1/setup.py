# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['django_static_markdown_blog',
 'django_static_markdown_blog.core',
 'django_static_markdown_blog.migrations']

package_data = \
{'': ['*'], 'django_static_markdown_blog': ['templates/*', 'templates/blog/*']}

install_requires = \
['beautifulsoup4>=4.6,<5.0',
 'django==2.0.6',
 'libaloha>=0,<1',
 'markdown>=2.6,<3.0',
 'redis>=2.10,<3.0']

setup_kwargs = {
    'name': 'django-static-markdown-blog',
    'version': '0.0.1',
    'description': 'Django application to create a blog based on local Markdown files',
    'long_description': None,
    'author': 'Aloha68',
    'author_email': 'dev@aloha.im',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
