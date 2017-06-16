from setuptools import setup

setup(
    name='example-Test',
    version='1.0',
    py_modules=['example-Test'],
    install_requires=[
        'click>=6.6,<6.7',
        'Flask>=0.11<0.12'
    ],
    entry_points='''
        [console_scripts]
        example=example:main
    ''',
)
