import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zeel-publisher",
    version="1.0.1",
    author="Zeel",
    author_email="hosting@zeel.com",
    description="A package for publishing to SNS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zeel-dev/zeel-publisher",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
