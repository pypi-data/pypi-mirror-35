import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tittles",
    version="0.0.1",
    author="Leon",
    author_email="le_ma_@mail.ru",
    description="Tittles package with small useful funcs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonmaks/tittles",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
