from setuptools import setup


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup(
    name='awsx-cli',
    version='1.1.0',
    author='Mert Öngengil, Mehmet Eraslan, Engin Can Höke',
    description='AWS credential management tool',
    long_description=long_description,
    long_description_content_type="text/markdown", 
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
