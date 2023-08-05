import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="czutil",
    version="0.0.1",
    author="zhengchengzi",
    author_email="zhangchangzeng163@gmail.com",
    description="utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.leitingpro.top",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)