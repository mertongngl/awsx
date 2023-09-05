from setuptools import setup

setup(
    name='awsx-cli',
    version='1.0',
    author='Mert Önengil, Mehmet Eraslan',
    description='AWS credential management tool',
    long_description='A Python script for managing AWS credentials.',
    url='https://github.com/mertongngl/awsx',
    py_modules=['awsx'],
    install_requires=[
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'awsx = awsx:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
