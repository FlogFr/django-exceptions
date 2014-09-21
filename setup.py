#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-exceptions',
    version='0.2',
    author='aRkadeFR',
    author_email='contact@arkade.info',
    url='http://arkadefr.github.io/',
    description='Django app to handle exceptions in a comfortable way',
    packages=['djexceptions'],
    package_dir={'': 'project'},
    classifiers=[
        'Framework :: Django',
    ],
)
