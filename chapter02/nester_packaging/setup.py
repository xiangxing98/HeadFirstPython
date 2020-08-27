# -*- encoding: utf-8 -*-
# !/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name='nester_hou', # Replace with your own username
    version='1.5.6',
    author='Stone_hou',
    author_email='stone_hou@smics.com',
    description='a simple printer of nested lists',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/xiangxing98',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# Packaging Python Projects

# Step 1
# cd /d F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter02\nester_packaging\

# Step 2
# python setup.py sdist bdist_wheel

# Step 3
# Win10 User Create a new file in user folder (.pypirc) and input:
# [testpypi]
#   username = __token__
#   password = pypi-AgENdGVzdC5weXBpLm9yZwIkN2E3NzBjODQtYzY2MS00OTU1LWFlZmEtNTU2NTBkODIxZDE3AAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDrCa49zLVP3atMlBGx755KKqlMFeLEAlxLkNJFSPPV4A

# Step 4
# python -m twine upload --repository testpypi dist/*

# Step 5
# pip install nester_hou
# python -m pip install --index-url https://test.pypi.org/simple/ --no-deps nester_hou