from setuptools import find_packages , setup
from typing import List

setup(
    name='sensore',
    version="0.0.1",
    author="dushyant",
    author_email="25007839d@gmail.com",
    packages=find_packages(),
    install_requires = ["pymongo"]
)