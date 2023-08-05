import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="asyncio-pubsub",
    version="0.0.1",
    author="Eirik Tenold",
    author_email="eirik@relativt.net",
    description="Simple implementation of a more asyncio friendly Google Pubsub client that can be used with aiohttp.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)