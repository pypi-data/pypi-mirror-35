from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='unittest-hooks',
      version=version,
      description="pre commit hook for unittest",
      long_description="""\
used to run unittests on python project on /tests/unittests path""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='unittest pre-commit ut',
      author='Nanthakumar',
      author_email='splnanthakumar@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
