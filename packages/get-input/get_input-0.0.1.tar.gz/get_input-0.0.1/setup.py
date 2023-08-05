import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = "get_input",
    version = "0.0.1",
    author = "Prashant Sengar",
    author_email = "prashantsengar5@hotmail.com",

    description = "This package allows program to get data iput of a specific type without giving errors",

    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/yoptgyo/get_input",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

