import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="red9",
    version="0.0.1",
    author="Farsheed Ashouri",
    author_email="rodmena@me.com",
    description="Python APIs for using RED9 Service Delivery Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ourway/red9",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
