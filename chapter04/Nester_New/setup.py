# -*- encoding: utf-8 -*-
# !/usr/bin/env python
import setuptools

with open("README.md", "r", encoding ='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(

    name='nester_hou', 
	# 软件包的名称。该名称由字母，数字，_和-组成。
	# 并且不能与其他已经上传至pypi.org的项目相同

    version='1.5.7',
	# version: 软件包的版本
	
    author='Stone_hou',
	# 软件包的作者
	
    author_email='stone_hou@smics.com',
	# 软件包作者邮箱地址
	
    description='a simple printer of nested lists',
	# 软件包的描述信息
	
    long_description=long_description,
	# 软件包的长描述信息
	
    long_description_content_type="text/markdown",
	# 软件包的长描述信息，内容
	
    url='https://github.com/xiangxing98',
	# 软件包的主页链接,常见的github路径较多
	
    packages=setuptools.find_packages(),
	# 包含在发布软件包文件中的可被import的python包文件。
	# 我们可以手动罗列所有文件。
	# 或者使用函数setuptools.find_packages()自动包含所有的python包文件以及子包文件
	
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	# 当前软件包的其他元数据信息(metadata)。
	# 例如兼容的python版本和操作系统；提供的功能的类型及许可证等等。
	# 应当总是至少包括当前软件包所支持的python版本，操作系统和许可证信息
	
    python_requires='>=3.6',
	# 指定了当前软件包所依赖的其他python类库。
	# 这些指定的python类库将会在本package被安装的时候一并被安装
)

# Packaging Python Projects

# Step 1
# cd /d F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter04\Nester_New\

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

# Step 6 Offline install
# cd /d F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter04\Nester_New\dist
# pip install nester_hou-1.5.6-py3-none-any.whl