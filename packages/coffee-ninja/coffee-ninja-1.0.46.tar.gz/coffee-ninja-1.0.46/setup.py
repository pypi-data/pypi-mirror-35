import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="coffee-ninja",
    version="1.0.46",
    author="CoffeeNinja",
    description="Coffee Ninja",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://example.com/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    )
)
