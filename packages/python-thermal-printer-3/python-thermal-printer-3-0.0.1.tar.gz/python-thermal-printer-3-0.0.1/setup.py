import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-thermal-printer-3",
    version="0.0.1",
    author="Conor Matthews",
    author_email="conormatthews6@gmail.com",
    description="The Adafruit thermal printer library ported for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ConorMatthews/Python-Thermal-Printer/tree/Python3andRaspberryPi3",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
