import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fair_flow",
    version="0.0.1",
    author="Joe Fair",
    author_email="joe@fairanswers.com",
    description="Simple Workflow Library",
#    long_description=long_description,
#    long_description_content_type="text/markdown",
    url="https://fairanswers.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
