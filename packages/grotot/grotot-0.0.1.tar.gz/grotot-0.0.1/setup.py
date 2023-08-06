from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'PDE solver'
LONG_DESCRIPTION = 'A package that solves ...'

# Setting up
setup(
    name="grotot",
    version=VERSION,
    author="Sachin S. Rawat, Shawan K. Jha",
    author_email="<sachinr@iitk.ac.in>, <shawankumar@iitg.ac.in>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy','matplotlib', 'tqdm'],
    keywords=['python', 'gpe', 'gpu'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)