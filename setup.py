#!/usr/bin/env python

from distutils.core import setup

setup(
    name='more.chameleon',
    version='0.1',
    description='Chameleon template renderer for MorePath',
    author='Izhar Firdaus',
    author_email='kagesenshi.87@gmail.com',
    url='http://github.com/koslab/more.static',
    package_dir={'':'src'},
    packages=['more', 'more.chameleon'],
    license='MIT',
    install_requires=[
        'morepath>=0.9',
        'more.static',
    ]
)
