import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fanchart",
    version="0.0.1dev",
    author="Dialid Santiago ",
    author_email="d.santiago@outlook.com",
    description="Fan Charts Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quantgirluk/fanchart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['twopiece','numpy>=1.13.1', 'scipy>=0.19.1', 'matplotlib>=2.2.2', 'seaborn>=0.8'],
)
