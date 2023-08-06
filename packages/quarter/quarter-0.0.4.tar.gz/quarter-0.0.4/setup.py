import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quarter",
    version="0.0.4",
    author="Patrick Fant",
    author_email="patrick.fant@recordedfuture.com",
    description="datetime-like package to work with financial quarters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PatrickFant/quarter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
