#from distutils.core import setup
#from distutils.extension import Extension
from setuptools import setup
from setuptools.extension import Extension

import subprocess

import os

#update version
args = 'git describe --tags'
p = subprocess.Popen(args.split(), stdout=subprocess.PIPE)
version = p.communicate()[0].decode("utf-8").strip()

#version = "0.1.8"
#version = "0.1.9" # Fix file extensions
version = "0.2.0" # Minor changes

#lines = open('grizli/version.py').readlines()
version_str = """# git describe --tags
__version__ = "{0}"\n""".format(version)
fp = open('hsaquery/version.py','w')
fp.write(version_str)
fp.close()
print('Git version: {0}'.format(version))

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "hsaquery",
    version = version,
    author = "Gabriel Brammer",
    author_email = "gbrammer@gmail.com",
    description = "Python tools for querying the ESA Hubble Science Archive",
    license = "MIT",
    url = "https://github.com/gbrammer/esa-hsaquery",
    download_url = "https://github.com/gbrammer/esa-hsaquery/tarball/{0}".format(version),
    packages=['hsaquery'],
    classifiers=[
        "Development Status :: 1 - Planning",
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
    ],
    install_requires=[
         'astropy>=2.0.0',
         'lxml>=3.8.0',
         'numpy>=1.10.2',
         'geos>=0.2.1',
         'shapely>=1.5.16',
         'matplotlib>=2.0.2',
         'descartes>=1.0.2'
    ],
    package_data={'hsaquery': []},
)
