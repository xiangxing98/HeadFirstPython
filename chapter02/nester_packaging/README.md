# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Generating distribution archives

### Step 1 Make sure you have the latest versions of setuptools and wheel installed

#### change directory

```{bash}
## Running Code:
cd /d F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter02\nester_packaging\
python setup.py
```

#### run code

```{bash}
python -m pip install --user --upgrade setuptools wheel
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple

# Requirement already up-to-date: setuptools in d:\programfiles\anaconda3\lib\site-packages (49.6.0.post20200814)
# Requirement already up-to-date: wheel in # c:\users\xiang\appdata\roaming\python\python37\site-packages (0.35.1)
```

#### setup

Now run this command from the same directory where setup.py is located:

```{python}
python setup.py sdist bdist_wheel

running sdist
running egg_info
creating nester_hou.egg-info
writing nester_hou.egg-info\PKG-INFO
writing dependency_links to nester_hou.egg-info\dependency_links.txt
writing top-level names to nester_hou.egg-info\top_level.txt
writing manifest file 'nester_hou.egg-info\SOURCES.txt'
reading manifest file 'nester_hou.egg-info\SOURCES.txt'
writing manifest file 'nester_hou.egg-info\SOURCES.txt'
running check
creating nester-hou-1.5.2
creating nester-hou-1.5.2\nester_hou.egg-info
creating nester-hou-1.5.2\nester_pkg
copying files to nester-hou-1.5.2...
copying README.md -> nester-hou-1.5.2
copying setup.py -> nester-hou-1.5.2
copying nester_hou.egg-info\PKG-INFO -> nester-hou-1.5.2\nester_hou.egg-info
copying nester_hou.egg-info\SOURCES.txt -> nester-hou-1.5.2\nester_hou.egg-info
copying nester_hou.egg-info\dependency_links.txt -> nester-hou-1.5.2\nester_hou.egg-info
copying nester_hou.egg-info\top_level.txt -> nester-hou-1.5.2\nester_hou.egg-info
copying nester_pkg\__init__.py -> nester-hou-1.5.2\nester_pkg
Writing nester-hou-1.5.2\setup.cfg
creating dist
Creating tar archive
removing 'nester-hou-1.5.2' (and everything under it)
running bdist_wheel
running build
running build_py
creating build
creating build\lib
creating build\lib\nester_pkg
copying nester_pkg\__init__.py -> build\lib\nester_pkg
installing to build\bdist.win-amd64\wheel
running install
running install_lib
creating build\bdist.win-amd64
creating build\bdist.win-amd64\wheel
creating build\bdist.win-amd64\wheel\nester_pkg
copying build\lib\nester_pkg\__init__.py -> build\bdist.win-amd64\wheel\.\nester_pkg
running install_egg_info
Copying nester_hou.egg-info to build\bdist.win-amd64\wheel\.\nester_hou-1.5.2-py3.7.egg-info
running install_scripts
adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
creating build\bdist.win-amd64\wheel\nester_hou-1.5.2.dist-info\WHEEL
creating 'dist\nester_hou-1.5.2-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'nester_pkg/__init__.py'
adding 'nester_hou-1.5.2.dist-info/LICENSE'
adding 'nester_hou-1.5.2.dist-info/METADATA'
adding 'nester_hou-1.5.2.dist-info/WHEEL'
adding 'nester_hou-1.5.2.dist-info/top_level.txt'
adding 'nester_hou-1.5.2.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
```

This command should output a lot of text and once completed should generate two files in the dist directory:

dist/
  example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz

## Step 2 Uploading the distribution archives

Finally, it's time to upload your package to the Python Package Index!

The first thing you'll need to do is register an account on Test PyPI. Test PyPI is a separate instance of the package index intended for testing and experimentation. It's great for things like this tutorial where we don't necessarily want to upload to the real index. To register an account, go to <https://test.pypi.org/account/register/> and complete the steps on that page. You will also need to verify your email address before you're able to upload any packages. For more details on Test PyPI, see Using TestPyPI.

### register account

<https://test.pypi.org/account/register/>
Name: siqin
Email Address: xiangxing985529@163.com
Username (required): siqin

### Verify email

Your primary email address (xiangxiang985529@163.com) is unverified. Verify your email or add a new address.

Done

### Create a new API token

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

### Using this token

To use this API token:

Set your username to __token__
Set your password to the token value, including the testpypi- prefix

For example, if you are using Twine to upload your projects to PyPI, set up your $HOME/.pypirc file like this.

Win10 User Create a new file in user folder: .pypirc and input:

```{python}
[testpypi]
  username = __token__
  password = pypi-AgENdGVzdC5weXBpLm9yZwIkN2E3NzBjODQtYzY2MS00OTU1LWFlZmEtNTU2NTBkODIxZDE3AAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDrCa49zLVP3atMlBGx755KKqlMFeLEAlxLkNJFSPPV4A
```

### Use twine to upload the distribution packages

to install Twine first

```{bash}
python -m pip install --user --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:

```{bash}
python -m twine upload --repository testpypi dist/*
```

You will be prompted for a username and password. For the username, use __token__.
For the password, use the token value, including the pypi- prefix.

## Installing your newly uploaded package

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
