from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'basic package'

# Setting up
setup(
    name="fiiireflyyy",
    version=VERSION,
    author="fiiireflyyy (Willy Lutz)",
    author_email="<lutz0willy@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['scikit-learn',],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)