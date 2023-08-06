import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name		= "hmpnester",
    version		= "1.2.0",
    author		= "hmperez",
    author_email	= "betomperez@gmail.com",
    description		= "Tutorial package from HeadFirst series",
    long_description	= long_description,
    long_description_content_type="text/markdown",
    url			= "",
    packages		= setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
