from setuptools import setup, find_packages

with open("README.md", "r") as fh:

    long_description = fh.read()


setup(
    name="bulkhead",
    version="0.1.5",
    packages=find_packages(include=["bulkhead*"]),
    include_package_data=True,
    author="Julian M. Kleber",
    author_email="julian.m.kleber@gmail.com",
    description="package providing objects for API interaction",
    install_requires=["python-dotenv"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.codeberg/cap_jmk/prettify-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
