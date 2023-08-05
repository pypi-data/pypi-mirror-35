import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nauth_sdk",
    version="0.0.4",
    author="ntkomata",
    author_email="ntkomata@outlook.com",
    description="A simple sdk for nauth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)