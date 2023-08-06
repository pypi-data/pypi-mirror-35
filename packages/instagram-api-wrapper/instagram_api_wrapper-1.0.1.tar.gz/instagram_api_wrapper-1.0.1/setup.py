import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="instagram_api_wrapper",
    version="1.0.1",
    author="Yevgenii Kaidashov",
    author_email='zhenya.kaidashov@gmail.com',
    description="Instagram api wrapper",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/YevgeniiKaidashov/instagram_api_wrapper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    install_requires=[
        'requests'
    ]
)
