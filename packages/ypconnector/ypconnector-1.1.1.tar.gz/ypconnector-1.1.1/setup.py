import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ypconnector",
    version="1.1.1",
    author="YappesLib",
    author_email="info@yappes.com",
    description="Python SDK for integrating APIs published via Yappes platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yappes-technologies/ypconnector-python",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)