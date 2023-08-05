import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indentpy",
    version="1.0.0",
    author="Thijs van Ede",
    author_email="t.s.vanede@utwente.nl",
    description="Python utility to change indentations of files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thijsvanede/indentpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
