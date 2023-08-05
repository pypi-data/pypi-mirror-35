import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AutoParam",
    version="0.0.1",
    author="Vrishank Bhardwaj",
    author_email="vrishank1997@gmail.com",
    description="An RL based HyperParameter Optimiser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vrishank97/AutoParam",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
