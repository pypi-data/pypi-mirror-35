import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="twitter_analytics",
    version="0.0.1",
    author="Philippe Oger",
    author_email="phil.oger@gmail.com",
    description=("A twitter analytics reports downloader. The only way to get tweet impressions data"),
    license="MIT",
    keywords="twitter analytics reports downloader",
    url="http://someurl.com/",
    packages=['twitter_analytics'],
    install_requires=[
        'selenium',
        'python-dateutil',
        'pyvirtualdisplay'
    ],
    long_description=read('README.md')
)
