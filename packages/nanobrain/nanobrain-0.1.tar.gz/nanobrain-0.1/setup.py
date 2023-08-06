from setuptools import setup

setup(
    name='nanobrain',
    version='0.1',
    description='Smart troubleshooting assistant for coders <nanobrain.io>',
    author='Samandar Ravshanov',
    url='https://nanobrain.io',
    py_modules=['nb'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        nb=nb:cli
    ''',
)

