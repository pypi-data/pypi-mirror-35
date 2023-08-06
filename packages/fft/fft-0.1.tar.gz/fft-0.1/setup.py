import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fft",
    version="v0.1",
    author="Monty Dimkpa",
    author_email="cmdimkpa@gmail.com",
    description="FFT: Teaching functional programming with a funds transfer example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cmdimkpa/fft/archive/v0.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
