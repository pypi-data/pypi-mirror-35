from setuptools import setup, find_packages

setup(
    name='genius-cli2',
    version='1.0.17',
    packages=find_packages(),

    url='',
    license='Private',
    author='Alex Rudakov',
    author_email='alex@negative.ee',
    description='Genius generator.',
    long_description='',

    install_requires=[
        'click',
        'requests',
        'termcolor',
        'beautifulsoup4',
        'pyparsing',
        'jinja2',
    ],

    entry_points={
        'console_scripts': [
            'genius = genius_cli.main:run',
        ]
    },
)

