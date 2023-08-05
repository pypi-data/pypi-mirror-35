import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="winauto",
    version="0.0.7",
    author="TheCornerPiece",
    author_email="cornerpieceofficial@gmail.com",
    description="A simple Windows module to simulate user input (written in C)",
    long_description=long_description,
    url="https://github.com/thecornerpiece/winauto",
    packages=setuptools.find_packages('winauto'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
