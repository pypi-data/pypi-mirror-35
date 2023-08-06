import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sapass",
    version="1.9",
    author="hasan sajedi",
    author_email="hassansajedi@gmail.com",
    description="With this module you can easy generate password in python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hasansajedi/sapass",
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)