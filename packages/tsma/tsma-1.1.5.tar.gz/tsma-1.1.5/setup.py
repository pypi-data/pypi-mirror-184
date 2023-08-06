# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:14:59 2023

@author: S-bazaz
"""
__author__ = ["Samuel Bazaz"]
__credits__ = ["Samuel Bazaz"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = ["Samuel Bazaz"]

##############
#  Packages  #
##############
from setuptools import setup, find_namespace_packages


# Load the README file
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()
setup(
    # Define the library name, this is what is used along with `pip install`.
    name="tsma",
    # Define the author of the repository.
    author="S-bazaz",
    # Define the Author's email, so people know who to reach out to.
    author_email="sbazazj2@protonmail.com",
    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version="1.1.5",
    description="""(time series model analyses) This package offers tools for analyzing models that generate multivariate time series as output.""",
    long_description=long_description,
    # This will specify that the long description is MARKDOWN.
    long_description_content_type="text/markdown",
    # Here is the URL where you can find the code, in this case on GitHub.
    url="https://github.com/S-bazaz/tsma",
    license="MIT",
    # These are the dependencies the library needs in order to run.
    install_requires=[
        "dash==2.6.1",
        "dash_bootstrap_components==1.2.1",
        "iisignature==0.24",
        "jupyter_dash==0.4.2",
        "matplotlib==3.5.1",
        "networkx==2.8.8",
        "numpy==1.21.5",
        "pandas==1.4.3",
        "plotly==5.9.0",
        "scikit_learn==1.2.0",
        "scipy==1.7.3",
        "seaborn==0.11.2",
        "statsmodels==0.13.2",
        "tqdm==4.64.0",
        "tslearn==0.5.2",
    ],
    keywords="time-series-analysis, phase-diagram, time-series-clustering, simulated-dataset",
    packages=find_namespace_packages(include=["tsma", "tsma.*"]),
    include_package_data=True,
    # package_data={
    #     # And include any files found subdirectory of the "td" package.
    #     "td": ["app/*", "templates/*"],
    # },
    py_modules=[
        "tsma",
        "tsma.basics",
        "tsma.analyses",
        "tsma.collect",
        "tsma.models",
        "tsma.visuals",
    ],
    python_requires=">=3.7",
    # Additional classifiers that give some characteristics about the package.
    # For a complete list go to https://pypi.org/classifiers/.
    classifiers=[
        # I can say what phase of development my library is in.
        "Development Status :: 3 - Alpha",
        # Here I'll add the audience this library is intended for.
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Other Audience",
        # Here I'll define the license that guides my library.
        "License :: OSI Approved :: MIT License",
        # Here I'll note that package was written in English.
        "Natural Language :: English",
        # Here I'll note that any operating system can use it.
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: OS Independent",
        # Here I'll specify the version of Python it uses.
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        # Here are the topics that my library covers.
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Office/Business :: Financial",
        "Framework :: Pytest",
    ],
)
