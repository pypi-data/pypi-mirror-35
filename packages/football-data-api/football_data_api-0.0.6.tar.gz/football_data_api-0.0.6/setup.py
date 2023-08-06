import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="football_data_api",
    version="0.0.6",
    author="Miquel Vande Velde",
    author_email="miquel.vandevelde@gmail.com",
    url='https://github.com/miquel-vv/football_data_api',
    keywords=['football', 'data', 'football-data.org'],
    description="Python interface for the football-data.org api from Daniel.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)