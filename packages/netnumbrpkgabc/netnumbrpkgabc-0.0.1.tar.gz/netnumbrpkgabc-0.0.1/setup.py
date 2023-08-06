from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A python number package'
LONG_DESCRIPTION = 'A python library which stores a set of numbers within a range.'

# Setting up
setup(
    name="netnumbrpkgabc",
    version=VERSION,
    author="Nqobile Ngwenya",
    author_email="<nqobilehunchongwenya@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

