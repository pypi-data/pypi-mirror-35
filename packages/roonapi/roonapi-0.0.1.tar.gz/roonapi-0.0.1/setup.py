# Used this guide to create module
# http://peterdowns.com/posts/first-time-with-pypi.html

# git tag 0.1 -m "0.1 release"
# git push --tags origin master
#
# Upload to PyPI Live
# python setup.py register -r pypi
# python setup.py sdist upload -r pypi

import setuptools

VERSION = "0.0.1"
NAME = "roonapi"
INSTALL_REQUIRES = ["websocket-client"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    author='Marcel van der Veldt',
    author_email='marcelveldt@users.noreply.github.com',
    description='Provides a python interface to interact with Roon',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/marcelveldt/python-roon.git',
    packages=['roon'],
    classifiers=(
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ),
    package_data = {'': ['.soodmsg'] },
    install_requires=INSTALL_REQUIRES,
    )