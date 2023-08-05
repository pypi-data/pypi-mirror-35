import sys; sys.path.append("tfinterface")

import os
from setuptools import setup, find_packages
from version import __version__



# parse requirements
with open('requirements.txt') as f:
    reqs = f.read().splitlines()


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(
    name = "tfinterface",
    version = __version__,
    author = "Cristian Garcia",
    author_email = "cgarcia.e88@gmail.com",
    description = ("A light wrapper over TensorFlow that enables you to easily create complex deep neural networks using the Builder Pattern through a functional fluent immutable API"),
    license = "MIT",
    keywords = ["tensorflow", "deep learning", "neural networks"],
    url = "https://github.com/cgarciae/tfinterface",
   	packages = find_packages(),
    package_data={
        '': ['LICENCE', 'requirements.txt', 'README.md', 'CHANGELOG.md'],
        'tfinterface': ['README-template.md']
    },
    download_url = 'https://github.com/cgarciae/tfinterface/tarball/{0}'.format(__version__),
    include_package_data = True,
    long_description = read('README.md'),
    install_requires = reqs
)
