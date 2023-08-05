import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lfdeploy",
    version="1.0",
    author="Przemyslaw Winszczyk",
    description="Improved tfdeploy module",
    url="https://github.com/LendFlo/Lendflo-tfdeploy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)