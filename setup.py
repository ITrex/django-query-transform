#!/bin/env python
# -*- coding: utf-8 -*-

'''URL query string manipulation template tags for django template engine'''

import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-query-transform',
    version='0.1',
    packages=['django_query_transform', 'django_query_transform.templatetags'],
    include_package_data=True,
    description=locals()['__doc__'],
    url='https://github.com/ITrex/django-query-transform',
    author='Renat Galimov',
    author_email='renat2017@Gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],

    install_requires=(
        'Django==1.6.5'
    ),
)
