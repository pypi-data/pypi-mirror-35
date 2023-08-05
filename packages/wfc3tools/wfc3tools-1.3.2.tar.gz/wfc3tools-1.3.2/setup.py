#!/usr/bin/env python
import os
import subprocess
import sys
from setuptools import setup, find_packages

try:
    from distutils.config import ConfigParser
except ImportError:
    from configparser import ConfigParser

conf = ConfigParser()
conf.read(['setup.cfg'])

# Get some config values
metadata = dict(conf.items('metadata'))
PACKAGENAME = metadata.get('package_name', 'wfc3tools')
DESCRIPTION = metadata.get('description', '')
AUTHOR = metadata.get('author', 'STScI')
AUTHOR_EMAIL = metadata.get('author_email', 'help@stsci.edu')
URL = metadata.get('url', 'https://wfc3tools.readthedocs.io/')
LICENSE = metadata.get('licesnce', 'BSD')

if os.path.exists('relic'):
    sys.path.insert(1, 'relic')
    import relic.release
else:
    try:
        import relic.release
    except ImportError:
        try:
            subprocess.check_call(['git', 'clone',
                                   'https://github.com/jhunkeler/relic.git'])
            sys.path.insert(1, 'relic')
            import relic.release
        except subprocess.CalledProcessError as e:
            print(e)
            exit(1)


version = relic.release.get_info()
relic.release.write_template(version, PACKAGENAME)

setup(
    name=PACKAGENAME,
    version=version.pep386,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'astropy',
    ],
    packages=find_packages(),
    package_data={PACKAGENAME: ['pars/*']}
)
