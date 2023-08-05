
from setuptools import setup, find_packages
from daydreamer import __version__

setup(
    name="daydreamer",
    version=__version__,
    author="Nick Georgiadis",
    author_email="nickgeo_@hotmail.com",
    description="Daydreamer Nick API Python wrapper",
    url="https://github.com/rozzac90/pinnacle",
    packages=['daydreamer'],
    install_requires=[line.strip() for line in open("requirements.txt")],
    long_description=open('README.md').read(),
    tests_require=['pytest'],
)
