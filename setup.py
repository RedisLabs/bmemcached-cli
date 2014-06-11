# #!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <andrew.w.gross@gmail.com> wrote this file. As long as you retain
# this notice you can do whatever you want with this stuff. If we meet
# some day, and you think this stuff is worth it, you can buy me a
# beer in return Poul-Henning Kamp
# ----------------------------------------------------------------------------
# Modified to support SASL (binary protocol) by <itamar@redislabs.com>
# http://redislabs.com
# ----------------------------------------------------------------------------

import os
from setuptools import setup


def get_packages():
    # setuptools can't do the job :(
    packages = []
    for root, dirnames, filenames in os.walk('bmemcachedcli'):
        if '__init__.py' in filenames:
            packages.append(".".join(os.path.split(root)).strip("."))

    return packages


setup(name='bmemcached-cli',
      version='0.1.0',
      description='memcached command line interface with SASL (binary protocol) support',
      author=u'Itamar Haber',
      author_email='itamar@redislabs.com',
      url='http://github.com/redislabs/bmemcached-cli',
      packages=['bmemcachedcli'],
      install_requires=[
          "python-binary-memcached",
      ],
      entry_points={
          'console_scripts': ['bmemcached-cli = bmemcachedcli.main:main'],
      },

)
