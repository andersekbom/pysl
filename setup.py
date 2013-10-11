try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PySL',
    'author': 'Anders Ekbom',
    'url': 'ekbom.org',
    'download_url': 'ekbom.org/download',
    'author_email': 'anders.ekbom@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pysl'],
    'scripts': [],
    'name': 'pysl'
}

setup(**config)
