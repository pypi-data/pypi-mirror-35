import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fair_flow",
    version="0.0.4",
    author="Joe Fair",
    author_email="joe@fairanswers.com",
    description="Simple Workflow Library",
    url="https://fairanswers.com",
    dependency_links=['https://github.com/timtadh/dot_tools'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
