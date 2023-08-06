import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bored",
    version="1.0.1",
    description="Unofficial Wrapper for Bored API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://henryb.uk",
    author="Henry Bersey",
    author_email="henry@bersey.com",
    packages=["bored"],
    install_requires=["requests"],
    zip_save=False
)