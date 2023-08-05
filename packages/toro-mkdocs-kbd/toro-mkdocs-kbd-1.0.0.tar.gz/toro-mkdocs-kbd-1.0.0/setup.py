import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="toro-mkdocs-kbd",
    version="1.0.0",
    author="TORO",
    description="A Python markdown extension for wrapping keyboard shortcuts in a special tag",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.torocloud.com/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    )
)
