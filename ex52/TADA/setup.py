try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'Frode Mikalsen',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'frodemikalsen@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TADA'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
