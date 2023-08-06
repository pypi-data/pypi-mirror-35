import setuptools

with open("README.md", "r") as fh: long_description = fh.read()

setuptools.setup(
    name="dbu",
    version="0.0.1",
    author="Le Ma",
    author_email="le_ma_@mail.ru",
    description="DB Utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonmaks/dbu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
