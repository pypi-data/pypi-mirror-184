import os
from setuptools import setup, find_packages
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), fname), "r") as fin:
        return fin.read()
setup(
    name = "cwbplot",
    version = "0.0.8",
    author = "cwbrfsteam",
    author_email = "littlepon4@hotmail.com",
    description = "Central weather bureau rfs team and open data useful tool for daily wrok.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license = "MIT",
    url = "https://github.com/Liu-CWB/cwbplot",
    project_urls={
        # 'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        # 'Funding': 'https://donate.pypi.org',
        'Source': "https://github.com/Liu-CWB/cwbplot",
        # 'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },
    #packages=find_packages(exclude=["tests*"]),
    packages=['cwbplot'],
    package_dir={'cwbplot': 'src/cwbplot'},
    package_data={'cwbplot': ['fonts/*.ttf','sharedata/*'],},
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.0.3",
        "numpy>=1.17.3",
        "matplotlib>=3.3.3,<3.5.0",
        "pygrib>=2.0.4",
        "requests>=2.25.0",
        "netcdf4>=1.5.6,<=1.6.0",
        "basemap>=1.3.0",
        "basemap-data>=1.3.0",
        "basemap-data-hires>=1.3.0",
        "xmltodict>=0.12.0",
    ],
    extras_require={
                 'geotiff':['gdal>=2.4.1']
                   },
    #setup_requires=[
    #     "pandas>=1.0.3",
    # ],
    # see http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        #"Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
    ],)
