# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Folder Structure

```
# tree
.
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── pg_client
│           ├── __init__.py
│           └── pg_operator.py
├── dist
│   ├── pypostgrestool-0.1-py3-none-any.whl
│   └── pypostgrestool-0.1.tar.gz
├── LICENSE
├── pg_client
│   ├── __init__.py
│   └── pg_operator.py
├── pypostgrestool.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
└── setup.py

# Another Folder Structure
tidy_page
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├──tidypage
│   ├──cleaners.py
│   ├──extractor.py
│   ├──__init__.py
│   └──titles.py
 
```

`dist`下的文件是需要上传到pypi下的

整理代码的目录结构，方便打包和python的import，为了方便引用，需要将代码模块变成一个包，所以需要将功能代码用目录来整合方便引用，并且需要创建`__init__.py`文件，`__init__.py`中可以没有内容，也可以在`__init__.py`文件中进行import（from .extractor import Document）操作，以减少整体模块引用时import的层数，避免错误。

- LICENSE文件是授权文件，比如：MIT license， APACHE license

- README.md 文件想必大家都不陌生，其实就是项目介绍和使用说明

- setup文件才是重点，是python模块安装所需要的文件，它的格式如下：

## setup.py

```python
#!/usr/bin/env python
from os.path import abspath, dirname, join 
from __future__ import print_function
from setuptools import setup, find_packages
import sys

# 这下面几行是做了小小的封装, 可以先跳过直接看 `setup()` 函数部分
MIDDLEWARE_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# meta_file = open(os.path.join(MIDDLEWARE_BASE_DIR, "django_jaeger_middleware", "metadata.py")).read()
# md = dict(re.findall(r"__([a-z]+)__\s*=\s*'([^']+)'", meta_file))  # 读取 metadata.py 文件

with open(os.path.join(MIDDLEWARE_BASE_DIR, 'README.md'),'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tidy-page",
    version="0.1.1",
    author="Desion Wang",
    author_email="wdxin1322@qq.com",
    description="html text parser,get the content form html page",
    long_description=long_description,
    license="MIT",
    url="https://github.com/desion/tidy_page",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        lxml_requirement
        ],
	keywords=['django', 'jaeger', 'jaegertracing'], 
    classifiers=[
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     python_requires='>=3.6',
)

# NAME 名字，一般放你包的名字即可
# PACKAGES 包含的包，可以多个，这是一个列表
# DESCRIPTION 关于这个包的描述
# LONG_DESCRIPTION 参见read方法说明
# KEYWORDS 关于当前包的一些关键字，方便PyPI进行分类。
# AUTHOR 谁是这个包的作者，写谁的名字吧
# AUTHOR_EMAIL 作者的邮件地址
# URL 你这个包的项目地址，如果有，给一个吧，没有你直接填写在PyPI你这个包的地址也是可以的
# VERSION 当前包的版本，这个按你自己需要的版本控制方式来
# LICENSE 授权方式
# INSTALL_REQUIRES 模块所依赖的python模块

# 文中的classifiers的内容并不是随便填写的，你需要参照本文参考文档中的PyPI Classifiers来写
```



## Generating distribution archives

### Step 1 Make sure you have the latest versions of setuptools and wheel installed

#### change directory

```{bash}
# Running Code:
cd /d F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter02\nester_packaging\

# python setup.py
```

#### run code**安装依赖**

```{bash}
python -m pip install --user --upgrade pip twine setuptools wheel

# Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
# Requirement already up-to-date: setuptools in d:\programfiles\anaconda3\lib\site-packages (49.6.0.post20200814)
# Requirement already up-to-date: wheel in # c:\users\xiang\appdata\roaming\python\python37\site-packages (0.35.1)
```

#### setup-开始使用Distutils进行打包

  为了保证效果，在打包之前我们可以验证setup.py的正确性，执行下面的代码

```python
python setup.py check
# 输出一般是running check
# 如果有错误或者警告，就会在此之后显示
# 没有任何显示表示Distutils认可你这个setup.py文件。那么就可以正式打包，执行下面的代码：
```

  Now run this command from the same directory where setup.py is located:

```{python}
python setup.py sdist bdist_wheel

# running sdist
# running egg_info
# creating nester_hou.egg-info
# writing nester_hou.egg-info\PKG-INFO
# writing dependency_links to nester_hou.egg-info\dependency_links.txt
# writing top-level names to nester_hou.egg-info\top_level.txt
# writing manifest file 'nester_hou.egg-info\SOURCES.txt'
# reading manifest file 'nester_hou.egg-info\SOURCES.txt'
# writing manifest file 'nester_hou.egg-info\SOURCES.txt'
# running check
# creating nester-hou-1.5.2
# creating nester-hou-1.5.2\nester_hou.egg-info
# creating nester-hou-1.5.2\nester_pkg
# copying files to nester-hou-1.5.2...
# copying README.md -> nester-hou-1.5.2
# copying setup.py -> nester-hou-1.5.2
# copying nester_hou.egg-info\PKG-INFO -> nester-hou-1.5.2\nester_hou.egg-info
# copying nester_hou.egg-info\SOURCES.txt -> nester-hou-1.5.2\nester_hou.egg-info
# copying nester_hou.egg-info\dependency_links.txt -> nester-hou-1.5.2\nester_hou.egg-info
# copying nester_hou.egg-info\top_level.txt -> nester-hou-1.5.2\nester_hou.egg-info
# copying nester_pkg\__init__.py -> nester-hou-1.5.2\nester_pkg
# Writing nester-hou-1.5.2\setup.cfg
# creating dist
# Creating tar archive
# removing 'nester-hou-1.5.2' (and everything under it)
# running bdist_wheel
# running build
# running build_py
# creating build
# creating build\lib
# creating build\lib\nester_pkg
# copying nester_pkg\__init__.py -> build\lib\nester_pkg
# installing to build\bdist.win-amd64\wheel
# running install
# running install_lib
# creating build\bdist.win-amd64
# creating build\bdist.win-amd64\wheel
# creating build\bdist.win-amd64\wheel\nester_pkg
# copying build\lib\nester_pkg\__init__.py -> build\bdist.win-amd64\wheel\.\nester_pkg
# running install_egg_info
# Copying nester_hou.egg-info to build\bdist.win-amd64\wheel\.\nester_hou-1.5.2-py3.7.egg-info
# running install_scripts
# adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
# creating build\bdist.win-amd64\wheel\nester_hou-1.5.2.dist-info\WHEEL
# creating 'dist\nester_hou-1.5.2-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
# adding 'nester_pkg/__init__.py'
# adding 'nester_hou-1.5.2.dist-info/LICENSE'
# adding 'nester_hou-1.5.2.dist-info/METADATA'
# adding 'nester_hou-1.5.2.dist-info/WHEEL'
# adding 'nester_hou-1.5.2.dist-info/top_level.txt'
# adding 'nester_hou-1.5.2.dist-info/RECORD'
# removing build\bdist.win-amd64\wheel
```

打包之后 会在项目的dist目录内生成whl文件. This command should output a lot of text and once completed should generate two files in the dist directory:

dist/
  example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz

执行完成后，会在顶层目录下生成dist目录和egg目录

```
tidy_page
├── tidy_page/dist
│   ├── tidy_page/dist/tidy-page-0.1.0.tar.gz
│   └── tidy_page/dist/tidy-page-0.1.1.tar.gz
├── tidy_page/LICENSE
├── tidy_page/README.rst
├── tidy_page/setup.py
├── tidy_page/tidypage
│   ├── tidy_page/tidypage/cleaners.py
│   ├── tidy_page/tidypage/extractor.py
│   ├── tidy_page/tidypage/__init__.py
│   └── tidy_page/tidypage/titles.py
├── tidy_page/tidy_page.egg-info
│   ├── tidy_page/tidy_page.egg-info/dependency_links.txt
│   ├── tidy_page/tidy_page.egg-info/PKG-INFO
│   ├── tidy_page/tidy_page.egg-info/requires.txt
│   ├── tidy_page/tidy_page.egg-info/SOURCES.txt
│   └── tidy_page/tidy_page.egg-info/top_level.txt
```



### Step 2 Uploading the distribution archives-**将whl文件上传到pypi服务器**

打包完成后就可以准备将打包好的模块上传到pypi了，首先你需要在pypi上进行注册 goto [PyPI Live](http://pypi.python.org/pypi?%3Aaction=register_form) 

Finally, it's time to upload your package to the Python Package Index!

The first thing you'll need to do is register an account on Test PyPI. Test PyPI is a separate instance of the package index intended for testing and experimentation. It's great for things like this tutorial where we don't necessarily want to upload to the real index. To register an account, go to <https://test.pypi.org/account/register/> and complete the steps on that page. You will also need to verify your email address before you're able to upload any packages. For more details on Test PyPI, see Using TestPyPI.

#### register account**注册pypi账号**

<https://test.pypi.org/account/register/>
Name: siqin
Email Address: xiangxing985529@163.com
Username (required): siqin

#### Verify email

Your primary email address (xiangxiang985529@163.com) is unverified. Verify your email or add a new address.

Done

#### Create a new API token

Now you'll create a PyPI API token so you will be able to securely upload your project.

Go to <https://test.pypi.org/manage/account/#api-tokens> and create a new API token; don't limit its scope to a particular project, since you are creating a new project.

```{bash}
Token name: nester
Permissions: Upload packages
Scope (required): Entire account(all projects)

Token:
pypi-AgENdGVzdC5weXBpLm9yZwIkN2E3NzBjODQtYzY2MS00OTU1LWFlZmEtNTU2NTBkODIxZDE3AAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDrCa49zLVP3atMlBGx755KKqlMFeLEAlxLkNJFSPPV4A
```

Don't close the page until you have copied and saved the token you won't see that token again.

Now that you are registered, you can use twine to upload the distribution packages. You'll need to install Twine:

#### Using this token-**pypirc模板** 

To use this API token:

Set your username to __token__
Set your password to the token value, including the testpypi- prefix

For example, if you are using Twine to upload your projects to PyPI, set up your $HOME/.pypirc file like this.



注册完成后，你需要在本地创建好pypi的配置文件，不然有可能会出现使用http无法上传到pypi的问题,这个文件用来存储刚才注册pypi账号信息

Create a `.pypirc` configuration file，在用户的home目录下创建.pypirc文件，文件的内容如下

Win10 User Create a new file in user folder: .pypirc and input, 

```{python}
[testpypi]
  username = __token__
  password = pypi-AgENdGVzdC5weXBpLm9yZwIkN2E3NzBjODQtYzY2MS00OTU1LWFlZmEtNTU2NTBkODIxZDE3AAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDrCa49zLVP3atMlBGx755KKqlMFeLEAlxLkNJFSPPV4A
```

#### Use twine to upload the distribution packages

to install Twine first

```{bash}
python -m pip install --user --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:

```{bash}
python -m twine upload --repository testpypi dist/*

# twine upload dist/*
# Uploading distributions to https://upload.pypi.org/legacy/
# Enter your username:
# 输入用户名和密码就能够上传到pypi下。
```

You will be prompted for a username and password. For the username, use __token__.
For the password, use the token value, including the pypi- prefix.

### Step 3 Installing your newly uploaded package

You can use pip to install your package and verify that it works.

Create a new virtualenv (see Installing Packages for detailed instructions) and install your package from TestPyPI:

```{bash}
# python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE

# Install OK
# python -m pip install --index-url https://test.pypi.org/simple/ --no-deps nester-hou-siqin
# Looking in indexes: https://test.pypi.org/simple/
# Collecting nester-hou-siqin
#   Downloading https://test-files.pythonhosted.org/packages/28/e1/cdca708023837c2fc7b628d363ae17fb44973073fe74be380fb3d663edcd/nester_hou_siqin-1.5.2-py3-none-any.whl (5.2 kB)
# Installing collected packages: nester-hou-siqin
# Successfully installed nester-hou-siqin-1.5.2

# Install OK
pip install nester_hou
# Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
# Collecting nester_hou
#   Downloading https://pypi.tuna.tsinghua.edu.cn/packages/6f/b2/aff1596f3c55371c46951d9cf5fdc684df19965bf6aa95390bccf5b7af62/nester_hou-2.0.1-py2.py3-none-any.whl (2.1 kB)
# Installing collected packages: nester-hou
# Successfully installed nester-hou-2.0.1
```

## Issues

### Issue 1

HTTPError: 403 Forbidden from <https://test.pypi.org/legacy/>
Invalid or non-existent authentication information. See <https://test.pypi.org/help/#invalid-auth> for more information.

### Issue 1 Solution

Win10 User Create a new file in user folder: .pypirc and input:

```{python}
[testpypi]
  username = __token__
  password = pypi-AgENdGVzdC5weXBpLm9yZwIkN2E3NzBjODQtYzY2MS00OTU1LWFlZmEtNTU2NTBkODIxZDE3AAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDrCa49zLVP3atMlBGx755KKqlMFeLEAlxLkNJFSPPV4A
```

### Issue 1 Solution & Result

```{bash}
F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter02\nester_packaging>python -m twine upload --repository testpypi dist/*
Uploading distributions to <https://test.pypi.org/legacy/>
Uploading nester_hou-1.5.2-py3-none-any.whl
100%|| 6.59k/6.59k [00:02<00:00, 3.03kB/s]
Uploading nester-hou-1.5.2.tar.gz
100%|| 5.55k/5.55k [00:00<00:00, 5.99kB/s]

View at:
<https://test.pypi.org/project/nester-hou/1.5.2/>
```
