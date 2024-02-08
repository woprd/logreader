import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

files_to_include = ['apache.log']

setuptools.setup(
    name="logreader",  
    version="0.1.0",  
    author="woprd",# NOTE: real username
    author_email="hello@woprd.com", # NOTE: not real email
    description="Reads Common Log Format files and does useful stuff with them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woprd/logreader",   
    packages=setuptools.find_packages(),   
    package_data={'logreader': files_to_include},
    # include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
    install_requires=["pandas"],
)
