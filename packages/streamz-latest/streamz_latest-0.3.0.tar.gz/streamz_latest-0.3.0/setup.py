#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import os
import codecs
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command


here = os.path.abspath(os.path.dirname(__file__))
packages = ['streamz', 'streamz.dataframe']

tests = [p + '.tests' for p in packages]

with open("README.rst", "r") as fh:
    long_description = fh.read()

class UploadCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except FileNotFoundError:
            pass
        self.status("Building Source distribution…")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))
        self.status("Uploading the package to PyPi via Twine…")
        os.system("sudo twine upload dist/*")
        sys.exit()


setup(name='streamz_latest',
      version='0.3.0',
      description='Mrocklin streamz library. It\'s the latest version ',
      url='http://github.com/mrocklin/streamz/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='streams',
      packages=packages + tests,
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      zip_safe=False,
      cmdclass={"upload": UploadCommand},
)
