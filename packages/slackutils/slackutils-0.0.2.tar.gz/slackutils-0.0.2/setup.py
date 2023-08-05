
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slackutils",
    version="0.0.2",
    author="Mads Wilthil",
    author_email="mads.wilthil@gmail.com",
    description="A small library to simplify slack web API calls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madsWilthil/slackutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)