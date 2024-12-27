from setuptools import setup, find_packages

__version__ = "0.0.1"

setup(
    name="cprint",
    version=__version__,
    author="Even Wong",
    author_email="wdyphy@zju.edu.cn",
    url="https://github.com/dotmet/cprint.git",
    description="A easy module for colorful print in Python.",
    long_description="",
    packages = find_packages(),
    zip_safe=False,
    python_requires=">=3.6",
)
