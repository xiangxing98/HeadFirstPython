# 修改Anaconda中Jupyter Notebook默认工作路径的详细图文教程（Win 10）

If you have Anaconda installed on your machine…then just type
conda install -c r r-essentials
 on your terminal & it will install R kernal as well as some of the important R packages (like dplyr, ggplot2 etc).
 For more details look at this link - https://www.continuum.io/blog/developer/jupyter-and-conda-r

## 1、运行Anaconda Prompt 生成jupyter_notebook_config.py配置文件

1.打开cmd，首先进入到Jupyter的安装目录，我的是在D:\ProgramFiles\Anaconda3\Scripts中。

然后，输入命令“jupyter notebook --generate-config”

```
cd /d D:\ProgramFiles\Anaconda3\Scripts

# 输入命令
jupyter notebook --generate-config
```

会在原工作目录中生成一个名为jupyter_notebook_config.py的文件（我的原工作目录为）


```
conda install -c r r-essentials
```


这个命令的作用是生成 Jupyter notebook 的配置文件。如果你是第一次运行，会直接生成这个文件。如果曾经运行过这个命令，就会像下图一样问你时候要覆盖原来的文件。这个时候不用理会。我们的主要目的只是为了找到这个文件的路径。
(base) C:\Users\xiang>jupyter notebook --generate-config
Writing default config to: C:\Users\xiang\.jupyter\jupyter_notebook_config.py

## 2、打开jupyter_notebook_config.py

找到 jupyter_notebook_config.py 的路径并打此文件。

找到 c.NotebookApp.notebook_dir 这个变量，将你希望的路径赋值给这个变量，并删除这一行前面的“#”。修改后如下：

```
## The directory to use for notebooks and kernels.
## c.NotebookApp.notebook_dir = 'F:\\Github\\Python\\01_Notebook'
c.NotebookApp.notebook_dir = 'F:\\Github\\Python\\HeadFirstPython\\HeadFirstPython'
```

#### 注意：

一定要确保删除 “#”，取消这一行的注释模式。
这一行代码前不能有空格。
路径一定要是已经存在的，否则会闪退。且路径要用英文单引号括起来。
路径一定'F:\\Github\\Python\\01_Notebook', 或者'F:/Github/Python/01_Notebook'

改完后保存。再次通过 Anaconda Navigator 进入 Jupyter Notebook 的时候会发现默认路径已经更改。

## 快捷方式设置更改

此时，如果你直接通过 Jupyter Notebook 的快捷方式进入，默认目录还是原来那个。

如果需要修改，还需要进行如下步骤：

找到快捷方式，右键打开属性，将“目标” 最后面的 “%USERPROFILE%” 删除就可以了。


## 我遇到的那些坑，及推测的原因：

1. 网上说打开 “cmd”，运行 “jupyter notebook --generate-config” 命令

可能是因为 Jupyter Notebook 是通过 Anaconda 安装的，所以 Anaconda 环境外没有配置环境变量。

2. 根据网上贴出的路径直接查找 “Jupyter_notebook_config.py” 文件，发现查无此文件。

再次提醒，如果从没运行过 generate 命令，是不会有这个配置文件的。

3. 据说，修改 Anaconda 安装目录下 etc\jupyter 文件夹中的 jupyter_notebook_config.json 文件也是可以的。但是，我的文件打开是这样的：

对，你没有看错，就是空的。我也不知道为什么。。。

4. 据说可以只改快捷方式的属性：“目标”那里的 “%USERPROFILE%” 删除，
D:\ProgramFiles\Anaconda3\python.exe D:\ProgramFiles\Anaconda3\cwp.py D:\ProgramFiles\Anaconda3 D:\ProgramFiles\Anaconda3\python.exe D:\ProgramFiles\Anaconda3\Scripts\jupyter-notebook-script.py %USERPROFILE%

“起始位置” %HOMEPATH% 改成你希望的路径F:\Github\Python\01_Notebook。

在不改 jupyter_notebook_config.py 文件的情况下，仅改变这两个地方，并不起任何作用。
如果改了 jupyter_notebook_config.py，这两个地方都不改的话，从这个快捷方式进入 Jupyter Notebook 会进入默认路径，用 Anaconda Navigator 启动就会进入改变后的路径。
对“目标”栏进行改动后，则从快捷方式进入，也会进入修改后的路径。“起始位置”那里的值，改不改都不影响。

## 修改默认浏览器
搜索‘c.NotebookApp.browser’，在下面增加以下语句：

```python
# import webbrowser
# webbrowser.register(
#     "chrome",  #自定义名字
#     None, 
#     webbrowser.GenericBrowser(u"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))#指定程序所在位置
# c.NotebookApp.browser = "chrome"

import webbrowser
webbrowser.register(
    "MSEdge",  #自定义名字
    None, 
    webbrowser.GenericBrowser(u"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))#指定程序所在位置
c.NotebookApp.browser = "MSEdge"
```



C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe



## conda config

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

注意：
添加完后，找到 .condarc 文件，删除里面的 defaults，这样能快点。

  - defaults
show_channel_urls: true

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

conda update conda



