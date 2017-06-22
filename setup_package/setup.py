from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Forecaster',
    version='1.0',
    license='MIT',
    keywords='wather forecast',
    description='Weather Forecaster',
    long_description=long_description,
    author='Rumen Neshev',
    author_email='neshev.rumen@abv.bg',
    py_packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'sample': ['package_data.dat'],
    },
    install_requires=[
        'click>=6.6,<=6.7'
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'forecaster=forecaster:main',
        ],
    },
)

# https://github.com/pypa/sampleproject

# https://www.youtube.com/watch?v=4fzAMdLKC5k

# 1. to install the package/module localy to be able to be developed
# $ pip install -e .


# 2. to install/update in otherwise:
# python setup.py install


# 3. to unsintall it - use the name
# $ pip uninstall Forecaster


# 4. Now it can be accessed from other Python modules with "import forecaster"
# for Windows it creates a new script EXE "forecaster.exe" in the python scripts folder
