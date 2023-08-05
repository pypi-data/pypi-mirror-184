# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sanic_beskar', 'sanic_beskar.orm']

package_data = \
{'': ['*'], 'sanic_beskar': ['templates/*']}

install_requires = \
['cryptography>=38.0.3,<39.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'passlib>=1.7,<2.0',
 'pendulum>=2.1,<3.0',
 'py-buzz>=3.2.1,<4.0.0',
 'pyjwt>=2.6,<3.0',
 'pyseto>=1.6.9,<2.0.0',
 'sanic>=22.6.0,<23.0.0']

setup_kwargs = {
    'name': 'sanic-beskar',
    'version': '2.2.6',
    'description': 'Strong, Simple, (now async!) and Precise security for Sanic APIs',
    'long_description': ".. image::  https://badge.fury.io/py/sanic-beskar.svg\n   :target: https://badge.fury.io/py/sanic-beskar\n   :alt:    Latest Published Version\n\n.. image::  https://github.com/pahrohfit/sanic-beskar/actions/workflows/main.yml/badge.svg\n   :target: https://github.com/pahrohfit/sanic-beskar/actions/workflows/main.yml\n   :alt:    Build Testing Status\n\n.. image::  https://img.shields.io/pypi/pyversions/sanic-beskar.svg\n   :target: https://img.shields.io/pypi/pyversions/sanic-beskar\n   :alt:    Supported Python versions\n\n.. image::  https://readthedocs.org/projects/sanic-beskar/badge/?version=latest\n   :target: http://sanic-beskar.readthedocs.io/en/latest/?badge=latest\n   :alt:    Documentation Build Status\n\n.. image::  https://codecov.io/gh/pahrohfit/sanic-beskar/branch/master/graph/badge.svg?token=24WAYX4OMT\n   :target: https://codecov.io/gh/pahrohfit/sanic-beskar\n   :alt:    Codecov Report\n\n.. image:: https://static.pepy.tech/personalized-badge/sanic-beskar?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads\n  :target: https://pepy.tech/project/sanic-beskar\n\n.. image::  https://api.codacy.com/project/badge/Grade/55f9192c1f584ae294bc1642b0fcc70c\n   :alt:    Codacy Badge\n   :target: https://app.codacy.com/gh/pahrohfit/sanic-beskar?utm_source=github.com&utm_medium=referral&utm_content=pahrohfit/sanic-beskar&utm_campaign=Badge_Grade_Settings\n\n.. image::  https://mayhem4api.forallsecure.com/api/v1/api-target/pahrohfit/pahrohfit-sanic-beskar/badge/icon.svg?scm_branch=master\n   :alt:    Mayhem for API\n   :target: https://mayhem4api.forallsecure.com/pahrohfit/pahrohfit-sanic-beskar/latest-job?scm_branch=master\n\n.. image::   https://img.shields.io/badge/security-bandit-yellow.svg\n    :target: https://github.com/PyCQA/bandit\n    :alt:    Security Status\n\n******************\n sanic-beskar\n******************\n\n* Stable branch: `master <https://github.com/pahrohfit/sanic-beskar/tree/master/sanic_beskar>`_\n* CBTE (coding by trial and error) branch: `dev <https://github.com/pahrohfit/sanic-beskar/tree/dev/sanic_beskar>`_\n* Working example(s): `examples/*.py <https://github.com/pahrohfit/sanic-beskar/tree/master/example>`_\n\n---------------------------------------------------\nStrong, Simple, and Precise security for Sanic APIs\n---------------------------------------------------\n\nThis project's begining was fully lifted from the awesome\n`Flask-Praetorian <https://github.com/dusktreader/flask-praetorian>`_.\n\nWhy `beskar <https://starwars.fandom.com/wiki/Beskar>`_? Why not -- what\nis better than star wars (provided you ignore the fact ~the mandolorian~\nwas almost as lame as ~book of boba fett~)?\nSuperior armour should be used if you want superior protection.\n\nThis package aims to provide that. Using token implemented by either\n`PySETO <https://pyseto.readthedocs.io/en/latest/>`_ or\n`PyJWT <https://pyjwt.readthedocs.io/en/latest/>`_,\n*sanic-beskar* uses a very simple interface to make sure that the users\naccessing your API's endpoints are provisioned with the correct roles for\naccess.\n\nThe goal of this project is to offer simplistic protection, without\nforcing nonsense, excessivly complicatated implimentation, or\nmandated/opinionated ORM usage. Providing this usability for small\nscaled Sanic applications, while allowing the flexibility and\nscalability for enterprise grade solutions, seperates this from your\nother options.\n\nThe *sanic-beskar* package can be used to:\n\n* Hash passwords for storing in your database\n* Verify plaintext passwords against the hashed, stored versions\n* Generate authorization tokens upon verification of passwords\n* Check requests to secured endpoints for authorized tokens\n* Supply expiration of tokens and mechanisms for refreshing them\n* Ensure that the users associated with tokens have necessary roles for access\n* Parse user information from request headers for use in client route handlers\n* Support inclusion of custom user claims in tokens\n* Register new users using email verification\n* Support OTP authentication as a dual factor\n* Provide RBAC based protection of endpoints and resources\n\nAll of this is provided in a very simple to configure and initialize flask\nextension. Though simple, the security provided by *sanic-beskar* is strong\ndue to the usage of the proven security technology of PASETO or JWT, along with\npython's `PassLib <http://pythonhosted.org/passlib/>`_ package.\n\nSuper-quick Start\n-----------------\n - requirements: `python` versions 3.7+\n - install through pip: `$ pip install sanic-beskar`\n - minimal usage example: `example/basic.py <https://github.com/pahrohfit/sanic-beskar/tree/master/example/basic.py>`_\n\nDocumentation\n-------------\n\nThe complete documentation can be found at the\n`sanic-beskar home page <http://sanic-beskar.readthedocs.io>`_\n",
    'author': 'Rob Dailey',
    'author_email': 'rob@suspected.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://sanic-beskar.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
