#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


__version__ = '0.1.0'


dependencies = {}
for env in ('prod', 'dev'):
    requires = []
    with open('requirements/{}.txt'.format(env)) as f:
        for line in f:
            if not (line.startswith('#') or line.startswith('-r')):
                requires.append(line)
    dependencies[env] = requires

with open('README.rst') as f:
    readme = f.read()


setup(
    name='cy',
    author='helms',
    author_email='zhanghdcy@gmail.com',
    url='https://github.com/helms/cy',
    description='cy website',
    long_description=readme,
    version=__version__,
    packages=find_packages(),
    install_requires=dependencies['prod'],
    tests_require=dependencies['dev'],
    extras_require={
        'dev': dependencies['dev'],
    }
)
