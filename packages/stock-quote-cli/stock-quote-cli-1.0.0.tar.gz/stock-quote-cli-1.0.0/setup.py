# coding: utf-8
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='stock-quote-cli',
    version = '1.0.0',
    author = 'yvvarun',
    author_email = 'yvvarun@gmail.com',
    description= 'show stock info',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/yvvarun/stock-quote-cli',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stock = stock.stock_quote:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
