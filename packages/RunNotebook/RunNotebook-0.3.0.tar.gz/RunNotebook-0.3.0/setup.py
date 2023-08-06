from setuptools import setup

setup(
    name="RunNotebook",
    version="0.3.0",
    author="Nathan Goldbaum",
    author_email="nathan12343@gmail.com",
    url="https://github.com/ngoldbaum/RunNotebook",
    packages=["RunNotebook"],
    install_requires=["sphinx", "jupyter", "nbconvert", "nbformat"]
)
