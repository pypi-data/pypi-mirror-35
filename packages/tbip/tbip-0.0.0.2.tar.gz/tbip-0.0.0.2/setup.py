import setuptools

with open("README.rst") as openfile:
    long_description = openfile.read()

setuptools.setup(
    name="tbip",
    version="0.0.0.2",
    author="Michael Gill",
    author_email="michael.78912.8@gmail.com",
    description="Build cross-platform installers",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/Michael78912/tbip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)