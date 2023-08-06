import setuptools

__author__ = None
__version__ = None

# Reading long description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# Reading __version__ and __author__ from __init__.py
with open("rs3clans/__init__.py") as f:
    exec(f.read())

AUTHOR = __author__
VERSION = __version__
NAME = 'rs3clans'
EMAIL = 'johnvictorfs@gmail.com'
DESCRIPTION = 'A Python 3 module wrapper for RuneScape 3 Clan\'s API'
URL = 'https://github.com/johnvictorfs/rs3clans.py'
REQUIRED = [
    'requests>=2.19.1',
]
REQUIRES_PYTHON = '>=3.6.0'

setuptools.setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    setup_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT',
    packages=setuptools.find_packages(exclude=('tests',)),
    zip_safe=False,
    url=URL,
    classifiers=(
        "Programming Language :: Python :: 3.6"
    )
)
