import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycodec",
    version="0.0.2",
    author="Denis Kotov (redradist, RedRadist, redra, RedRa)",
    author_email="redradist@gmail.com",
    description="PyCodec is a package for coding and decoding any message by any Coders and Decoders also as Crypto Coders and Crypto Decoders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/redradist/PyCodec.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)