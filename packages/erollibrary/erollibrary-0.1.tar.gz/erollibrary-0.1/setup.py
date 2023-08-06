import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from setuptools import setup

setup(
    name='erollibrary',  # This is the name of your PyPI-package.
    version='0.1',  # Update the version number for new releases
    scripts=['erol.py']
)
