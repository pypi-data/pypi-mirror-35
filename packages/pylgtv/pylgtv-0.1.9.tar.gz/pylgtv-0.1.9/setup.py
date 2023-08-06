import setuptools
from distutils.core import setup

with open("README.md", "r") as fh:
      long_description = fh.read()

setup(
      name = 'pylgtv',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages = ['pylgtv'],
      package_dir = {'pylgtv': 'pylgtv'},
      package_data = {'pylgtv': ['handshake.json']},
      install_requires = ['websockets', 'asyncio'],
      zip_safe = True,
      version = '0.1.9',
      description = 'Library to control webOS based LG Tv devices',
      author = 'Dennis Karpienski',
      author_email = 'dennis@karpienski.de',
      url = 'https://github.com/TheRealLink/pylgtv',
      download_url = 'https://github.com/TheRealLink/pylgtv/archive/0.1.9.tar.gz',
      keywords = ['webos', 'tv'],
      classifiers = [],
)
