'''setup.py'''

import os
import sys
from setuptools import setup, find_packages

def find_version():
    return '0.2.1'

# 'setup.py publish' shortcut.
if(sys.argv[-1] == 'publish'):
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
    description='An ultrafast audio time-scale modification library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Unlicense',
    url='https://github.com/WyattBlue/audiotsm2',
    author='WyattBlue',
    author_email='wyattbluesandbox@gmail.com',

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
