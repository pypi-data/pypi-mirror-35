import re

from setuptools import find_packages, setup

packages = find_packages(exclude=["tests*"])

version = re.search('^__version__\s*=\s*"(.*)"', open("ml_dev/__init__.py").read(), re.M).group(1)

setup(
    name="cognite-ml",
    version=version,
    description="Cognite Machine Learning Toolkit",
    url="https://github.com/cognitedata/ml_dev",
    download_url="https://github.com/cognitedata/ml_dev/archive/{}.tar.gz".format(version),
    author="Data Science Cognite",
    author_email="que.tran@cognite.com",
    packages=packages,
    install_requires=[],
    include_package_data=True,
)
