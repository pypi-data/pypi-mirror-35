import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CardRL",
    version="0.0.2",
    author="Vrishank Bhardwaj, Kartik Gupta",
    author_email="vrishank1997@gmail.com",
    description="A Python Card Game Environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vrishank97/CardRL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
