import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KinMSGUI",
    version="1.0.3",
    author="Tristan Burman",
    author_email="BurmanT@cardiff.ac.uk",
    description="GUI Interface for KinMS software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TristanBurman/KinMSGUI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)