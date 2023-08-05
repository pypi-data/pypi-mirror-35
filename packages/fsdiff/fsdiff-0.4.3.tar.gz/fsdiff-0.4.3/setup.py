#!/usr/bin/env python3

# Copyright (C) 2018 Ioannis Valasakis <code@wizofe.uk>
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2


from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='fsdiff',
    version='0.4.3',
    description='Byte to byte comparison of local disk images or filesystems',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ioannis Valasakis',
    author_email='code@wizofe.uk',
    url='https://github.com/wizofe/fsdiff',
    python_requires='>=3.0',
    packages=['fsdiff'],
    scripts=['bin/fsdiff'],
    install_requires=[
        "colorama"
    ],
    platforms='POSIX',
    license='GNU GPL v2'
)
