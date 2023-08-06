#!/usr/bin/env python

import sys
import os
import re
from setuptools import setup, find_packages

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass


def read(filename: str):
    fp = open(os.path.join(os.path.dirname(__file__), filename))
    text = fp.read()
    fp.close()
    return text


version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', read('pyganalytics/__init__.py'), re.MULTILINE).group(1)

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist')
    os.system('twine upload dist/pyganalytics-reporting-{}.tar.gz -r pypi'.format(version))
    sys.exit()

long_description = read('README.rst') + '\n\n\n' + read('LICENSE')

requires = read('requirements.txt').split('\n')

setup(
    name='pyganalytics-reporting',
    version=version,
    packages=find_packages(),
    url='https://github.com/Kordishal/pyganalytics-reporting',
    license='MIT',
    author='Jonas Waeber',
    author_email='jonaswaeber@gmail.com',
    description='A python wrapper for the Google Analytics Reporting API v4',
    long_description=long_description,
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],

)
