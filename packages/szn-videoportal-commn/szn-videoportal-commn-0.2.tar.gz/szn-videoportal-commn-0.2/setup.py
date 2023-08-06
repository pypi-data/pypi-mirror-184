from setuptools import find_packages, setup

setup(
    name="szn-videoportal-commn",
    version="0.2",
    maintainer="Ondrej Gersl",
    maintainer_email="ondra.gersl@seznam.cz",
    description="Package contains shared and handy tools for all our projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Topic :: Database",
    ],
)
