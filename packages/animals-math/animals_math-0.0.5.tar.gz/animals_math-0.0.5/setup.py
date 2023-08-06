import setuptools

import os
directory_name = os.path.abspath(os.path.dirname(__file__))
description = open(directory_name + "/README.md", 'r')
long_description = description.read()

setuptools.setup(
    name="animals_math",
    version="0.0.5",
    author="thunderB",
    author_email="thunderB@protonmail.com",
    licence="MIT",
    description="A package for animals and their math",
    long_description=long_description,
    url="https://github.com/thunder-B",
    packages=["animals", "animals.anims"]
)
