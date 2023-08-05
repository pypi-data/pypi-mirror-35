#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

try:
    with open('README.md') as f:
        readme = f.read()
except:
    readme = '''A small diary manager based on python.
Diapy uses cryptography.fernet to encrypt your top secret.'''

setup(
    name='diapy',
    version='3.0.0',
    description='A small diary manager based on python.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/FiftysixTimes7/diapy',
    author='FiftysixTimes7(PTJ)',
    author_email='pangtj26@163.com',
    license='MIT',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 3 :: Only',
                 'Topic :: Utilities'],
    keywords='diary',
    py_modules=['diapy'],
    python_requires='>=3.5.0',
    install_requires=['cryptography'],
)
