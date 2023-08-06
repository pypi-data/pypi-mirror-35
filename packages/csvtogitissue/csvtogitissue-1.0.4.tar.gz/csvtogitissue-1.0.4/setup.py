import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csvtogitissue",
    version="1.0.4",
    author="Sanjeven Ramakrishnan",
    author_email="sanjeven@gmail.com",
    description="A simple package to help convert CSV file entries to GITHub issues via API v3 (Private and Public repositories)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanjeven/CSV-to-GIThub-issue-creator",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)