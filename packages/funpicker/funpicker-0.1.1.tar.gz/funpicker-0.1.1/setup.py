from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="funpicker",
    version="0.1.1",
    author="Kevin Hill",
    author_email="kevin@funguana.com",
    description="A library to collect information for your trading bot. Use with `funtime` time series library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["funpicker"],
    install_requires=['cryptocompare', 'ccxt', 'requests'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    
)
