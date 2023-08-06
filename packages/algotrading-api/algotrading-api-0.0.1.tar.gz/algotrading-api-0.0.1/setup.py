import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algotrading-api",
    version="0.0.1",
    author="Jack Dry",
    author_email="jack_dry@outlook.com",
    description="A package to test trading algorithms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jdry1729/algo-trading",
    packages=setuptools.find_packages(),
    install_requires = [
        'matplotlib',
        'pandas',
        'termcolor',
        'numpy',
        'statsmodels'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
