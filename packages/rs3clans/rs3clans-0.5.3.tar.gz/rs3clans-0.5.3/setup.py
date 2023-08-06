import setuptools

NAME = 'rs3clans'
AUTHOR = 'John Victor'
EMAIL = 'johnvictorfs@gmail.com'
DESCRIPTION = 'A Python 3 module wrapper for RuneScape 3 Clan\'s API'
URL = 'https://github.com/johnvictorfs/rs3clans.py'
REQUIRED = [
    'requests>=2.19.1'
]
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.5.3'


with open("README.md", "r") as fh:
    long_description = fh.read()

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
        "Programming Language :: Python :: 3"
    )
)
