import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csc121",
    version="1.0.4",
    author="Raghuram Ramanujan",
    author_email="raramanujan@davidson.edu",
    description="Library for CSC 121 at Davidson College",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.davidson.edu/academics/mathematics-and-computer-science",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3',
    install_requires=[
        'numpy>=1.14.5',
        'scipy>=1.1.0',
        'Pillow>=5.2.0',
        'requests>=2.19.1',
        'py-getch>=1.0.1'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
