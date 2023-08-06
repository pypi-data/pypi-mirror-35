import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Aadhar",
    version="1.0.0",
    author="Nikhil Panwar",
    author_email="npanwar80@gmail.com",
    description="Python Library to validate and generate aadhar numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NikhilPanwar/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)