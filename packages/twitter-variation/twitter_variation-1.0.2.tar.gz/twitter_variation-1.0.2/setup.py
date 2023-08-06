import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitter_variation",
    version="1.0.2",
    author="Shubhanshu Sharma",
    author_email="dec31.shubh@gmail.com",
    description="A package to convert twitter variations into english letters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubhanshu786/twitter_variation",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
