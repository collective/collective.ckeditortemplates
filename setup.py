# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.3.4.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='collective.ckeditortemplates',
      version=version,
      description="Plone templates for ckeditor",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: Addon",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 6.0",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.10",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
      ],
      keywords='',
      author='IMIO',
      author_email='support@imio.be',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'beautifulsoup4',
          'Plone',
          'plone.app.contenttypes',
          'plone.api',
          'collective.ckeditor',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': [
          'Mock',
          'plone.app.robotframework',
          'robotframework-debuglibrary',
      ]},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
