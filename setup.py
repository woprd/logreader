import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

files_to_include = ['apache.log']

setuptools.setup(
    name="clfreader",  
    version="0.1.0",  
    author="woprd",
    author_email="hello@woprd.com",
    description="Reads Common Log Format files and does useful stuff with them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woprd/clfreader",   
    packages=setuptools.find_packages(),   
    package_data={'clfreader': files_to_include},
    # include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
    install_requires=["pandas"],
)
