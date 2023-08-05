from distutils.core import setup

setup(
  name = 'komorebi',
  packages = ['komorebi'],
  version = '0.0.5',
  description = 'Text Data API',
  author = 'Liling Tan',
  license = 'MIT',
  package_data={'komorebi': ['data/kopitiam/*']},
  url = 'https://github.com/alvations/komorebi',
  keywords = [],
  classifiers = [],
  install_requires = ['gensim', 'torch', 'bounter', 'pathlib']
)
