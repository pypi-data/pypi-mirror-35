import setuptools

with open("MicroTwisted/README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="MicroTwisted",
    version="0.0.1",
    author="Maximiliano Romay Figueroa",
    author_email="maximilianorom7@gmail.com",
    description="Micro Service Manager made with Twisted",
    long_description=readme,
    url="https://github.com/MaximilianoRom7/MicroTwisted",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
