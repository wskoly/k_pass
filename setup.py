from setuptools import setup, find_packages
import os

current_path = os.path.abspath(os.path.dirname(__file__))

def read_file(*parts):
    with open(os.path.join(current_path, *parts), encoding='utf-8') as reader:
        return reader.read()

VERSION = '0.0.2'
DESCRIPTION = 'Python package to generate random strong password and OTP.'

# Setting up
setup(
    name="k_pass",
    version=VERSION,
    url="https://github.com/wskoly/k_pass/",
    license="MIT",
    author="Wahid Sadique Koly",
    author_email="wskoly.bp@gmail.com",
    description=DESCRIPTION,
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'password', 'random', 'Random password', 'OTP'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)