# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['django_conditional_views', 'django_conditional_views.elements']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.1,<3.0']

extras_require = \
{u'docs': ['sphinx-autodoc-typehints>=1.3,<2.0', 'sphinx>=1.7,<2.0']}

setup_kwargs = {
    'name': 'django-conditional-views',
    'version': '0.1.3',
    'description': 'Simple Etag and Last-Modified mixins for class based views.',
    'long_description': "Django Conditional Views\n########################\n\n.. image:: https://circleci.com/gh/cordery/django-conditional-views.svg?style=svg\n  :target: https://circleci.com/gh/cordery/django-conditional-views\n  :alt: Build Status\n\n\n.. image:: https://codecov.io/gh/cordery/django-conditional-views/branch/master/graph/badge.svg\n  :target: https://codecov.io/gh/cordery/django-conditional-views\n  :alt: Test Coverage\n\n\n.. image:: https://readthedocs.org/projects/django-conditional-views/badge/?version=latest\n  :target: https://django-conditional-views.readthedocs.io/en/latest/?badge=latest\n  :alt: Documentation Status\n\n\n.. image:: https://img.shields.io/github/license/cordery/django-conditional-views.svg\n  :alt: MIT License\n\n\nSimple ETag and Last-Modified mixins for class based views.\n\n\nWhat is Django Conditional Views?\n==================================\n\nDjango Conditional Views builds off of the built in `django conditional view processing`_ machinery\nto provide simple mixins for class based views that implement support for the ETag and Last-Modified\nconditional request headers.\n\n.. _django conditional view processing: https://docs.djangoproject.com/en/2.1/topics/conditional-view-processing/\n\n\nFeatures\n========\n\nInherit one of these mixins to make your TemplateView's, DetailView's, or ListView's:\n\n  1. Calculate and append ETag and/or Last-Modified headers to the response and;\n\n  2. Respond with a `304 Not Modified`_ or a `412 Precondition Failed`_ to requests that provide conditional response headers such as If-Modified-Since\n\n.. _304 Not Modified: https://tools.ietf.org/html/rfc7232#section-4.1\n.. _412 Precondition Failed: https://tools.ietf.org/html/rfc7232#section-4.2\n\n**Helpful Defaults**\n  * ETags are automatically generated from the response.content.\n  * ETag generation can be customized both before and after the response is rendered.\n  * The Last Modified header is automatically set from the last modified timestamp of the template.\n  * In the case of the DetailView and ListView mixins, the Last Modified header may also be\n    configured to get the last modification timestamp from a field on the model, in which case\n    the lastest of that or the template's last modified timestamp will be used.\n\n\n\nGetting Started\n===============\n\n\nFirst install django-conditional-views\n\n.. code-block:: bash\n\n  $ pip install django-conditional-views\n\nThen inherit from one of the following mixins in your views:\n\n* ConditionalGetMixin - Inherits from View\n* ConditionalGetTemplateViewMixin - Inherits from TemplateView\n* ConditionalGetListViewMixin - Inherits from ListView\n* ConditionalGetDetailViewMixin - Inherits from DetailView\n\nSee the Usage_ and API_ sections of the documentation_ for more details.\n\n.. _Usage: https://django-conditional-views.readthedocs.io/en/latest/usage.html\n.. _API: https://django-conditional-views.readthedocs.io/en/latest/api.html\n.. _documentation: https://django-conditional-views.readthedocs.io/en/latest/\n\nContributing\n============\n\nContributions are welcome.\n\n\nGetting Started\n---------------\n\nTo work on the Pendulum codebase, you'll want to clone the project locally\nand install the required dependencies via `poetry <https://poetry.eustace.io>`_.\n\n.. code-block:: bash\n\n    $ git clone git@github.com:cordery/django-conditional-views.git\n    $ poetry develop\n\n\nRunning Tests\n---------------\ndjango-conditional-views uses pytest.  To run tests:\n\n.. code-block:: bash\n\n  $ pytest\n\n",
    'author': 'Andrew Cordery',
    'author_email': 'cordery@gmail.com',
    'url': 'https://github.com/cordery/django-conditional-views',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
