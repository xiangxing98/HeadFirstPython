# Visual Studio Code 输出中文出现乱码

如果直接这样运行 python 代码，会出现 print 打印出来的中文是乱码，要解决这个问题有三种办法：

**1. 增加系统全局变量**

以 windows 系统为例，添加系统变量：

```
PYTHONIOENCODING``=``UTF8
```

**2. 修改 VSC 配置文件**

F1 键调出控制台，输入task,选择任务：配置任务运行程序,打开tasks.json文件，增加以下信息：

```
"options"``: {`` ``"env"``:{`` ``"PYTHONIOENCODING"``: ``"UTF-8"`` ``}``}
```

**3.在代码里更改编码**

在每个需要中文的 python 文件中添加如下代码：

```
import` `io``import` `sys``#改变标准输出的默认编码``sys.stdout``=``io.TextIOWrapper(sys.stdout.``buffer``,encoding``=``'utf8'``)
```

使用方法1和方法2需要重启 VSC。

**方法1可以一劳永逸。**

以上这篇解决vscode python print 输出窗口中文乱码的问题就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。