from setuptools import setup, find_packages

__author__ = "Chen Kian Wee"
__copyright__ = "Copyright 2016, Chen Kian Wee"
__credits__ = ["Chen Kian Wee"]
__license__ = "GPL3"
__version__ = "0.12"
__maintainer__ = "Chen Kian Wee"
__email__ = "chenkianwee@gmail.com"
__status__ = "Development"

LONG_DESCRIPTION = "refer to https://github.com/chenkianwee/pyliburo for full installation instructions"
    
INSTALL_REQUIRES = ['lxml', 'pyshp', 'numpy', 'pycollada>=0.6', 'networkx', 'scikit-learn', 'pymf', 'matplotlib']

setup(name='pyliburo',
      packages = find_packages(),
      package_data={
          'pyliburo': ['databases/ettv/*.csv'],
          },
      version=__version__,
      description='Python Library for Urban Optimization',
      long_description=LONG_DESCRIPTION,
      author=__author__,
      author_email=__email__,
      url='https://github.com/chenkianwee/pyliburo',
      download_url = 'https://github.com/architecture-building-systems/pyliburo/archive/0.11.tar.gz',
      keywords = ["urban design", "architecture design", "design optimisation"],
      install_requires=INSTALL_REQUIRES,
      classifiers = ['Development Status :: 3 - Alpha',
                     'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                     'Programming Language :: Python :: 2.7',],
      )
