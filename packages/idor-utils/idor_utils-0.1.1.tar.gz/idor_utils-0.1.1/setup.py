import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="idor_utils",
    version="0.1.1",
    author="Bruno Melo",
    author_email="bruno.melo@idor.org",
    description="Package with utilities used in some projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/InstitutoDOr/utils_python.git",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)