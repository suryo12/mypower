import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypower-YASIRRONI", # Replace with your own username
    version="0.0.1",
    author="Muhammad Yasirroni",
    author_email="muhammadyasirroni@gmail.com",
    description="Supplementary function and Python port of MATPOWER",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yasirroni/myPower",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Scientific Engineering :: Mathematics",
    ],
    python_requires='>=3.6',
)
