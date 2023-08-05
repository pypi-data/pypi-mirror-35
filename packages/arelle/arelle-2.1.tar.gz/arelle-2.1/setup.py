import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arelle",
    version="2.1",
    author="Przemyslaw Winszczyk, Filip Duch, Remi Tuyaerts",
    author_email="n3onix@gmail.com",
    description="Light arelle package to extract xbrl files",
    url="https://github.com/LendFlo/Lendflo-arelle",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)