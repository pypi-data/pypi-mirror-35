import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="histopy",
    version="0.5.1",
    author="Daniel W. Paley",
    author_email="dwpaley@gmail.com",
    description="Bash-style history for Python interactive interpreter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dwpaley/history",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
