import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kpi_repository_client',
    version="1.0.0.3",
    author="REALTECH AG",
    author_email="info@realtech.com",
    description="Python client for KpiRepository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.realtech.com",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
