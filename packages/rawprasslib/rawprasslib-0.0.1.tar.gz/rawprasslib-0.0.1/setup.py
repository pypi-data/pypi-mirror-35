from setuptools import setup

with open("README.md", "r") as fh:
        long_description = fh.read()

setup(
    name="rawprasslib",
    version="0.0.1",
    author="Erik Andris, Jan Zelenka",
    author_email="3yanyanyan@gmail.com",
    description="Thermo/Finnigan .raw file format reader",
    long_decription=long_description,
    url="https://gitlab.science.ru.nl/jzelenka/rawprasslib",
    packages=['rawprasslib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
        ],
    requires=['numpy']
    )
