import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg_SWR_classTest",
    version="1.0.1",
    author="Sarah Winkler",
    author_email="sarah.winkler@initions-consulting.com",
    description="A small example package defining a test class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/pkg_SWR_classTest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)