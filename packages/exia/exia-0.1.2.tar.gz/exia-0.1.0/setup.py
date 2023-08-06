from setuptools import setup, find_packages

# Read the long description from the README.md file
with open("README.md", "r") as fh:
    long_description = fh.read()

# Define the package metadata
setup(
    name="exia",
    version="0.1.0",
    author="Thirakorn Mokkawes",
    author_email="thirakorn.mokkawes@manchester.ac.uk",
    description="A tool for preparing protein structures for simulation studies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/exia",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'argparse',
        'sys',
    ],
    entry_points={
        'console_scripts': [
            'exia=exia.exia:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
