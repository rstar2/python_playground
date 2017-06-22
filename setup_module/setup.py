from setuptools import setup

setup(
    name='ForecasterSimple',
    version='1.0',
    py_modules=['forecaster_simple'],
    install_requires=[
        'click>=6.6,<=6.7'
    ],
    entry_points='''
        [console_scripts]
        forecaster_simple=forecaster_simple:main
    ''',
)

# https://www.youtube.com/watch?v=4fzAMdLKC5k

# 1. to install the package/module localy to be able to be developed
# $ pip install -e .


# 2. to install/update in otherwise:
# python setup.py install


# 3. to unsintall it - use the name
# $ pip uninstall ForecasterSimple


# 4. Now it can be accessed from other Python modules with "import forecaster_simple"
# for Windows it creates a new script EXE "forecaster_simple.exe" in the python scripts folder
