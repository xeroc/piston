#!/usr/bin/env python

import sys
from setuptools import setup
import warnings
warnings.simplefilter('always', DeprecationWarning)

assert sys.version_info[0] == 3, "Piston requires Python > 3"

warnings.warn(
    "\n\n\n"
    "Deprecation warning"
    "\n"
    "Please use the `piston-cli` package instead of `steem-piston`!"
    "\n\n\n",
    DeprecationWarning
)

__VERSION__ = '0.4.9'

setup(
    name='steem-piston',
    version=__VERSION__,
    description='Command line tool to interface with the STEEM network (deprecated)',
    long_description=open('README.md').read(),
    download_url='https://github.com/xeroc/piston-cli/tarball/' + __VERSION__,
    author='Fabian Schuh',
    author_email='Fabian@chainsquad.com',
    maintainer='Fabian Schuh',
    maintainer_email='Fabian@chainsquad.com',
    url='http://cli.piston.rocks',
    keywords=['steem', 'library', 'api', 'rpc', 'cli'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    install_requires=[
        "piston-cli>=0.5.0",
    ],
)
