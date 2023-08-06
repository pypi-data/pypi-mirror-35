import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drestful",
    version="0.1",
    author="song.zirui",
    author_email="pochnsong@163.com",
    description="create simple django restful api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pochnsong/drestful",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)