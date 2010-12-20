#!/usr/bin/env python

from distutils.core import setup

setup(name='django-heroism',
      version='0.2',
      description='Middleware for SSL detection in Django, and context processor to redefinie media URL when the site runs behind Nginx as a proxy',
      author='Samuel Martin',
      author_email='martin.sam@gmail.com',
      url='http://github.com/martinsam/django-heroism/tree/master',
      packages=['heroism'],
)
