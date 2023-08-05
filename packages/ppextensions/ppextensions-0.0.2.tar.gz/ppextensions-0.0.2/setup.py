import os

from setuptools import setup, find_packages

DESCRIPTION = "PPExtenions - Set of iPython and Jupyter extensions"
NAME = "ppextensions"
AUTHOR = "PPExtensions Development Team"
AUTHOR_EMAIL = "jupyter@googlegroups.org"
URL = 'https://github.com/paypal/ppextensions'
DOWNLOAD_URL = 'https://github.com/paypal/ppextensions'
LICENSE = 'BSD License'

here = os.path.abspath(os.path.dirname(__file__))
README = """
# PPExtensions

PPExtensions is a suite of ipython and jupyter extensions built to improve user experience and reduce time to market in [Jupyter](http://jupyter.org) notebooks.


# Features

* **PPMagics ** - Set of magics to simplify access to different storage systems and tableau.
* **Github Integration ** - A jupyter extension to integrate notebooks with github. This extension simplifies version controlling, sharing and resolving merge conflicts of notebooks.
* **Notebooks Scheduling ** - A jupyter extension to productionalize the notebooks development environment. This extension enables scheduling notebooks with help of [airflow](https://airflow.apache.org/).
* **Config UI ** - A simple UI built to change the configurations of different extensions like PPMagic, [sparkmagic](https://github.com/jupyter-incubator/sparkmagic) ..etc.


# Installation

    pip install ppextensions


# Current State

| Feature              | Available   | State       |
|----------------------|-------------|-------------|
| PPMagics             | Available   | Beta        |
| Scheduling Notebooks | Coming soon | Coming soon |
| Github Integration   | Coming soon | Coming soon |
| Config UI            | Coming soon | Coming soon |

--------------------------------------------------------------------------------------------------------------------

# Documentation & Getting Started

    * [Click here to read the docs](http://ppextensions.readthedocs.io/)

# Questions

    * [Slack](https://ppextensions.slack.com)
    * [User Forum](https://groups.google.com/d/forum/ppextensions)
    * [Developer Forum](https://groups.google.com/d/forum/ppextensions)

"""

VERSION = '0.0.2'

install_requires = [
    'ipython>=1.0',
    'qgrid',
    'impyla==0.13.8',
    'hdfs3',
    'teradata==15.10.0.20',
    'protobuf==3.5.2.post1',
    'sqlparse',
    'pyhive==0.2.1',
    'pysftp==0.2.9',
    'tableausdk',
    'prettytable',
    'ipython-sql==0.3.8',
    'requests'
]

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=README,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=find_packages(),
      classifiers=[
          'Intended Audience :: System Administrators',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'],
      install_requires=install_requires,
      extras_require={
          'dev': [
              'pycodestyle'
          ]
      })
