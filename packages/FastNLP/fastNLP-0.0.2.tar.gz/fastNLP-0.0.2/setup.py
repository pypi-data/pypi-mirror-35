import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastNLP",
    version="0.0.2",
    author="Fudan FastNLP Team",
    author_email="fudanfastnlp@gmail.com",
    description="Deep Learning Toolkit for NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastnlp/fastnlp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
