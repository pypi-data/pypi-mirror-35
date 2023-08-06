import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secret-server-sdk-client",
    version="1.0",
    author="Paulo Dorado",
    author_email="support@thycotic.com",
    description="Thycotic python client that uses the Thycotic SDK to get secrets from secret server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thycotic/secret-server-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)