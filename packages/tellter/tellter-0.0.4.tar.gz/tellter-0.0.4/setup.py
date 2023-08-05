import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tellter",
    version="0.0.4",
    author="Tellter",
    author_email="contact@tellter.net",
    description="Tellter Official Public API - Currently supports TNS and Safechat.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://tellter.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)