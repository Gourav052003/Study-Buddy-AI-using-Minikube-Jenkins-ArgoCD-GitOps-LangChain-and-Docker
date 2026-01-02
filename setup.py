from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Study Buddy AI",
    version="0.0.0",
    author="Gourav",
    packages=find_packages(),
    install_requires=requirements 
)