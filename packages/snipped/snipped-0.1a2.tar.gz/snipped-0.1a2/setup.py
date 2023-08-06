import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snipped",
    version="0.1a2",
    author="Fabrizio Destro",
    author_email="destro.fabrizio@gmail.com",
    description="A small snippets manager.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dexpota/snip",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'snip=snipped.main:main',
        ],
    },
    classifiers={
        "Programming Language :: Python :: 3.5"
    },
    install_requires=[
        "docopt",
        "pyyaml",
        "pygments",
        "requests"],
)
