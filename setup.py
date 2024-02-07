import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
    install_requires=[   
    ],
    extras_require={   
    },
)
