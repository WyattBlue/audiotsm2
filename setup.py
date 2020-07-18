#!/usr/bin/env python3

import os
import re
import sys
from setuptools import setup, find_packages

def find_version():
    version_filename = os.path.abspath('audiotsm2/__init__.py')
    with open(version_filename) as fileobj:
        version_content = fileobj.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('rm -rf build')
    os.system('rm -rf dist')
    os.system('python3 setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='audiotsm2',
    version=find_version(),
    description='A real-time audio time-scale modification library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/WyattBlue/audiotsm2',
    author='WyattBlue',
    author_email='wyattbluesandbox@gmail.com',

    packages=find_packages(),

    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
