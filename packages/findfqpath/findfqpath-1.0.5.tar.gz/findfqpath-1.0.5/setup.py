import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="findfqpath",
    version="1.0.5",
    author="KevinSource",
    author_email="kdoglio@gmail.com",
    description="Package for findfqpath",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KevinSource/FindFQPath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['findfqpath.py']
)