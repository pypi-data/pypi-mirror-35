import os
import setuptools

ROOT = os.path.dirname(__file__)

with open(os.path.join(ROOT,"requirements","requirements.txt")) as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datawig",
    version="0.0.1",
    author="datawig-dev",
    author_email="datawig-dev@amazon.com",
    maintainer_email='datawig-dev@amazon.com',
    description="Imputation for tables with missing values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awslabs/datawig",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only'
    ],
)

