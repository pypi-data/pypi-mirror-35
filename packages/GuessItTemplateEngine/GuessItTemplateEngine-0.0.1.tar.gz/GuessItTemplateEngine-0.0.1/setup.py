import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

long_description = ''

setuptools.setup(
    name="GuessItTemplateEngine",
    version="0.0.1",
    author="online6731",
    author_email="mohammad.parsian@gmail.com",
    description="template engine for guess it project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)