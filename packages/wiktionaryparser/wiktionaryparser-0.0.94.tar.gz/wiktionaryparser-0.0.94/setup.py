from setuptools import setup,find_packages

with open('wiktionaryparser/readme.md', 'r') as readme:
  long_desc = readme.read()

setup(
  name = 'wiktionaryparser',
  version = '0.0.94',
  description = 'A tool to parse word data from wiktionary.com into a JSON object',
  long_description = long_desc,
  packages = ['wiktionaryparser', 'wiktionaryparser.tests', 'wiktionaryparser.utils'],
  data_files=[('testOutput', ['wiktionaryparser/tests/testOutput.json'])],
  author = 'Suyash Behera',
  author_email = 'sne9x@outlook.com',
  url = 'https://github.com/Suyash458/WiktionaryParser', 
  download_url = 'https://github.com/Suyash458/WiktionaryParser/archive/master.zip', 
  keywords = ['Parser', 'Wiktionary'],
  install_requires = ['beautifulsoup4','requests'],
  classifiers=[
   'Development Status :: 5 - Production/Stable',
  ],
)