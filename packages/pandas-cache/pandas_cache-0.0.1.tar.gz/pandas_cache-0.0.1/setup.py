from setuptools import setup, find_packages

setup(
    name="pandas_cache",  # this line is important.
    author="Zach Estela",
    author_email="z@aracel.io",
    install_requires=["pandas"],  
    packages=find_packages(),  
    url="https://github.com/N2ITN/pandas_cache",
    decription="decorator for smart caching of results from functions that return pandas DataFrames",
    zipsafe=False,
    version="0.0.1",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"),
)