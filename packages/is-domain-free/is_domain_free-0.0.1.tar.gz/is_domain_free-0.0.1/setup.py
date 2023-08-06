import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="is_domain_free",
    version="0.0.1",
    author="Marc-Olivier Gosselin",
    author_email="mogosselin@gmail.com",
    description="Simple package to check if 1 or more domain names are available.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mogosselin/is_domain_free",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
