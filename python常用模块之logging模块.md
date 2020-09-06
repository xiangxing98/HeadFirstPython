# [python常用模块之logging模块](https://www.cnblogs.com/yscl/articles/10046479.html)

> [logging模块](https://www.cnblogs.com/yscl/articles/10046479.html#3211030121) https://www.cnblogs.com/yscl/articles/10046479.html

logging模块是python内置模块中比较重要的模块，在日常调试，显示信息中有着重要作用。相比经常用的print函数，logging有着许多无与伦比的优势:

　　1. logging日志可以分级输出，从低到高有着5个等级，可以在不同的环境中输出不同的日志

　　2. logging日志可以输出到标准输出，文件，甚至通过soket,http等通过网络传输到其他机器上。

　　3. logging模块的格式化功能也非常强大，可以加上时间，线程名，日志所在行数等等

　　4. 当简单的分级输出已经不能满足条件时，logging日志甚至可以自定义过滤器过滤要输出的信息。

 

### logging模块详细用法[#](https://www.cnblogs.com/yscl/articles/10046479.html#1823703047)

**目录结构**

- [基础用法](https://www.cnblogs.com/yscl/articles/10046479.html#1)
- [写入文件](https://www.cnblogs.com/yscl/articles/10046479.html#2)
- [Handler和Formatter对象的使用](https://www.cnblogs.com/yscl/articles/10046479.html#3)
- [输出到文件、控制台、socket](https://www.cnblogs.com/yscl/articles/10046479.html#4)
- [日志回滚 ](https://www.cnblogs.com/yscl/articles/10046479.html#5)
- [记录异常信息](https://www.cnblogs.com/yscl/articles/10046479.html#6)
- [多模块共用同一配置](https://www.cnblogs.com/yscl/articles/10046479.html#7)
- [使用配置文件配置logging模块](https://www.cnblogs.com/yscl/articles/10046479.html#8)
- [过滤器的使用](https://www.cnblogs.com/yscl/articles/10046479.html#9)

 

####  0. 日志等级[#](https://www.cnblogs.com/yscl/articles/10046479.html#1120592804)

日志等级如下表所示，最低是notset，最高是critical

| **logging日志输出等级** |           |
| ----------------------- | --------- |
| **level**               | **value** |
| CRITICAL                | 50        |
| FATAL                   | 50        |
| ERROR                   | 40        |
| WARNING                 | 30        |
| WARN                    | 30        |
| INFO                    | 20        |
| DEBUG                   | 10        |
| NOTSET                  | 0         |

#### 1. 基础的用法[#](https://www.cnblogs.com/yscl/articles/10046479.html#3451857184)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging
# This function does nothing if the root logger already has handlers configured for it.
# logging.warning('warning')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - [line:%(lineno)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# log
logging.info('info')
logging.error('error')
logging.debug('debug')
logging.warning('warning')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 控制台输出（注意basicConfig函数有一个坑，该函数设置之前不能调用logging.info等函数输出，否则此处的设置便不起作用）

```
2018-11-30 20:54:20 - root - INFO - [line:13] - info
2018-11-30 20:54:20 - root - ERROR - [line:14] - error
2018-11-30 20:54:20 - root - DEBUG - [line:15] - debug
2018-11-30 20:54:20 - root - WARNING - [line:16] - warning
```

此处直接调用logging记录日志，因为basicConfig函数设置的输出等级是debug，所以根据分级表，大于等于debug的信息都将被输出到控制台。其中basicConfig函数有许多参数，它的其他参数如下表所示:

　　

| **参数** | **描述**                                                     |
| -------- | ------------------------------------------------------------ |
| filename | 日志输出的文件名称，如果指定了这项，就直接输出到文件中了，而不会再输出到控制台了。 |
| filemode | 与filename配套使用，指定文件的打开方式，默认是追加方式       |
| format   | 指定日志的输出格式，可以输出日期，日志行数等等。             |
| datefmt  | 指定时间输出的格式, 同[time.strftime()](https://docs.python.org/3/library/time.html#time.strftime)的输出格式。[``](https://docs.python.org/3/library/time.html#time.strftime) |
| style    | 指定格式化内容的占位符style，可以是"%","{","$"等，默认是%。  |
| level    | 指定root记录器的输出级别，默认是warnning及以上。             |
| stream   | 指定日志的输出流，默认是stderr，其他可以是sys.stdout或是文件，当filename和stream参数共存时，会抛出ValueError异常。 |
| handlers | 必须是由已经创建好的handles组成的一个可迭代的对象。把这些handlers添加到root记录器中。 |

如上面日志的format可以输出非常复杂的内容，format已经定义好的格式如下所示（更详细的可以参考[官方文档](https://docs.python.org/3/library/logging.html?highlight=logging#logrecord-attributes)）：

| **格式**        | **描述**                                                     |
| --------------- | ------------------------------------------------------------ |
| %(asctime)s     | 输出时间格式如 ‘2003-07-08 16:49:45,896’ 最后是毫秒          |
| %(created)f     | 日志创建的时间戳                                             |
| %(filename)s    | 当前执行的脚本名称                                           |
| %(funcName)s    | 输出当前日志的函数名                                         |
| %(levelname)s   | 日志输出的级别名称 ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL') |
| %(levelno)s     | 日志输出级别对应的具体数字大小 (DEBUG, INFO,WARNING, ERROR, CRITICAL) |
| %(lineno)d      | 输出当前日志在代码里的行数                                   |
| %(message)s     | 要输出的具体日志信息                                         |
| %(module)s      | 当前所在的模块名                                             |
| %(msecs)d       | 日志创建时的毫秒数                                           |
| %(name)s        | 当前日志记录器的名称，默认调用的是root日志记录器             |
| %(pathname)s    | 执行当前执行脚本的绝对路径                                   |
| %(process)d     | 进程id                                                       |
| %(processName)s | 当前进程名称                                                 |
| %(Thread)s      | 线程id                                                       |
| %(threadName)s  | 线程名称                                                     |

 

#### 2. 写入文件[#](https://www.cnblogs.com/yscl/articles/10046479.html#2070794532)

写入文件中也很简单，只要指定filename参数，logging信息便会输出到文件中。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - [line:%(lineno)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='testlog.log',
    )

    # log
    logging.info('info')
    logging.error('error')
    logging.debug('debug')
    logging.warning('warning')


if __name__ == '__main__':
    main()
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

文件testlog.log中内容为指定格式的时间，当前日志记录器的名称(默认的root), 日志级别，和输出的信息。

```
2018-11-30 22:53:33 - root - INFO - [line:13] - info
2018-11-30 22:53:33 - root - ERROR - [line:14] - error
2018-11-30 22:53:33 - root - DEBUG - [line:15] - debug
2018-11-30 22:53:33 - root - WARNING - [line:16] - warning
```

#### 3.Handler和Formatter对象的使用[#](https://www.cnblogs.com/yscl/articles/10046479.html#4158464553)

主要是创建一个logger记录对象，用这个logger对象输出信息，它可以添加各种handler以应用到不同的场景中，每一个handler可以单独设置的格式，即可以创建一个formatter对象。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging
import sys


# 创建log对象
logger = logging.getLogger(__name__)                # 这里不再用默认的root了, 而是自己创建一个日志记录器(logger), 名称可以自己随意起
logger.setLevel(logging.DEBUG)                      # 设置默认级别debug

# 创建formatter对象
fmt = '%(asctime)s - %(name)s - %(levelname)s - [line:%(lineno)s] - %(message)s'
formatter = logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S')

# 创建控制台的handler
console_handler = logging.StreamHandler(sys.stdout)  # 创建一个流handler,绑定到标准输出，默认是stderr
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)              # 为handler单独配置输出的格式
logger.addHandler(console_handler)                   # 将handler加到logger对象中

# log
logger.info('This info msg')
logger.debug('This is debug msg')
logger.warning('warning warning... ')
logger.error('Send a error msg!!!')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
2018-11-30 23:07:46 - __main__ - INFO - [line:20] - This info msg
2018-11-30 23:07:46 - __main__ - DEBUG - [line:21] - This is debug msg
2018-11-30 23:07:46 - __main__ - WARNING - [line:22] - warning warning... 
2018-11-30 23:07:46 - __main__ - ERROR - [line:23] - Send a error msg!!!
```

logging模块还提供了许多其他的handler来输出日志，其中StreamHandler和FileHandler位于logging模块下，其余皆位于logging.handlers模块下，详情可以参考[官方文档logging.handlers](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers)

- StreamHandler：日志输出到流，可以是 sys.stderr，sys.stdout 或者文件。
- FileHandler：日志输出到文件。
- BaseRotatingHandler：基本的日志回滚方式。（一般只用以下两种）
- RotatingHandler：日志回滚方式，支持日志文件最大数量和日志文件回滚。
- TimeRotatingHandler：日志回滚方式，在一定时间区域内回滚日志文件。
- SocketHandler：远程输出日志到TCP/IP sockets。
- DatagramHandler：远程输出日志到UDP sockets。
- SMTPHandler：远程输出日志到邮件地址。
- SysLogHandler：日志输出到syslog。
- NTEventLogHandler：远程输出日志到Windows NT/2000/XP的事件日志。
- MemoryHandler：日志输出到内存中的指定buffer。
- HTTPHandler：通过”GET”或者”POST”远程输出到HTTP服务器。

#### 4.日志同时输出到控制台、文件、tcp socket服务器[#](https://www.cnblogs.com/yscl/articles/10046479.html#2501620417)

在logger对象中添加StreamHandler,SocketHandler,FileHandler

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import sys
import logging.handlers


# 创建log对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建formatter对象
fmt = '%(asctime)s - %(name)s - %(levelname)s - [line:%(lineno)s] - %(message)s'
formatter = logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S')

# 创建控制台的handler
console_handler = logging.StreamHandler(sys.stdout)                 # 绑定到标准输出，默认是stderr
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 创建文件的handler
file_handler = logging.FileHandler('testlog.log')                   # 默认方式为追加方式a
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)                                # 给文件handle添加格式化对象
logger.addHandler(file_handler)

# 创建一个socket handler
socket_handler = logging.handlers.SocketHandler('localhost', 8000)  # tcp端口位于8000
socket_handler.setLevel(logging.WARNING)
logger.addHandler(socket_handler)

# log
logger.info('This info msg')
logger.debug('This is debug msg')
logger.warning('warning warning... ')
logger.error('Send a error msg!!!')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

tcp接收端的代码如下所示, socket用法参考官方文档[SocketHandler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler)和[Logging-cookbook](https://docs.python.org/3/howto/logging-cookbook.html#sending-and-receiving-logging-events-across-a-network)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import socket
import pickle
import struct

# tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8000))                     # 绑定本机8000端口
s.listen(8)
print('waiting for connections...')
while 1:
    # 无限循环等待接收客户端连接
    sock, addr = s.accept()
    while 1:
        chunk = sock.recv(4)                    # 发送端会添加4个字节的长度
        if len(chunk) < 4:
            break
        slen = struct.unpack('>L', chunk)[0]    # 将长度解包, 网络传输统一是大端, L代表无符号长整数
        chunk = sock.recv(slen)                 # 接收数据
        obj = pickle.loads(chunk)               # 反序列化, 系统默认发送的是序列化后的字节流
        print('接收到的数据：')
        # print(obj)            　　　　　　　　　 # 输出一个字典
        print('levelName: ', obj['levelname'])
        print('msg: ', obj['msg'])
    sock.close()
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

运行代码前tcp接收端也要运行。控制台输出如下

```
2018-11-30 23:25:58 - __main__ - INFO - [line:31] - This info msg
2018-11-30 23:25:58 - __main__ - DEBUG - [line:32] - This is debug msg
2018-11-30 23:25:58 - __main__ - WARNING - [line:33] - warning warning... 
2018-11-30 23:25:58 - __main__ - ERROR - [line:34] - Send a error msg!!!
```

文件中的内容:

```
2018-11-30 23:25:58 - __main__ - INFO - [line:31] - This info msg
2018-11-30 23:25:58 - __main__ - WARNING - [line:33] - warning warning... 
2018-11-30 23:25:58 - __main__ - ERROR - [line:34] - Send a error msg!!!
```

tcp接收端接收到的内容如下所示

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
waiting for connections...
接收到的数据：
levelName:  WARNING
msg:  warning warning... 
接收到的数据：
levelName:  ERROR
msg:  Send a error msg!!!
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 5.日志回滚 [#](https://www.cnblogs.com/yscl/articles/10046479.html#3338543843)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging.handlers


logger = logging.getLogger('')
logger.setLevel(logging.INFO)

rotate_handler = logging.handlers.RotatingFileHandler('日志回滚.log', maxBytes=40, backupCount=3)
formatter = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s %(message)s')
rotate_handler.setFormatter(formatter)
logger.addHandler(rotate_handler)

console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

logger.info('info info')
logger.error('error----')
logger.debug('debug~~~')
logger.warning('warning!!!!!')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

运行，可以看到当前文件夹的结构多出了几个文件。这是因为设置了备份文件为3个，当日志内容输出到文件中，超出了最大字节时，就会往备份文件里写入，这是按照文件大小进行对日志进行分割，还有一种按照时间分割删除过期文件，也是常用的一种回滚方式。

.
├── log_rotating.py
├── 日志回滚.log
├── 日志回滚.log.1
├── 日志回滚.log.2
└── 日志回滚.log.3

#### 6. 记录异常信息[#](https://www.cnblogs.com/yscl/articles/10046479.html#3933048971)

在程序中，想要保留遇到的异常信息，并将之输出到文件可以给logger.error()函数添加命名参数exc_info=True即可把错误轨迹均输出出来

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging


formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)
logger.addHandler(console)


file_handler = logging.FileHandler('error.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('Start')
try:
    1/0
except Exception:
    # logger.error('Something failed', exc_info=True)   # 此处写法同下面一样
    logger.exception('Exception occurred')
logger.info('Finished')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

文件控制台输出如下所示，清楚的显现出了错误信息

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
2018-12-01 00:22:47,057 root         INFO     Start
2018-12-01 00:22:47,057 root         ERROR    Exception occurred
Traceback (most recent call last):
  File "/home/yscl/python3_learn/logging_module/record_exception.py", line 21, in <module>
    1/0
ZeroDivisionError: division by zero
2018-12-01 00:22:47,058 root         INFO     Finished
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 7. 多模块共用同一配置[#](https://www.cnblogs.com/yscl/articles/10046479.html#3110757819)

main.py

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging
import auxiliary


logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)

logger.info('Start log')
logger.debug('something debug')
logger.error('something error')

auxiliary.func()
logger.info('Finished')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

auxiliary.py

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging

def func():
    logger = logging.getLogger('main.auxiliary')

    logger.info('auxiliary info')
    logger.debug('auxiliary debug')
    logger.error('auxiliary error')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

所谓多模块共用配置，是指在主模块里创建了一个名为main的logger，并为这个logger做了详细配置。在同一个python解释器进程中，可以复用名为main的logger，而不用重新配置一遍。在其他模块中可以定义main logger的子logger皆可以共享父logger的配置了。这里的父子logger是根据名字来判断的，比如父logger叫main，子logger就是main.xxx等任意以main开头的。

#### 8. 使用配置文件配置logging模块[#](https://www.cnblogs.com/yscl/articles/10046479.html#3237738668)

在开发中，在程序中写死配置是非常不便的，这也不利于维护和管理，所以从文件中读取配置就非常有必要了。python中支持从字典中加载logging的配置，所以可以用json或yaml来加载数据。json可读性相对来说没有yaml好，所以这里选择从yaml文件加载logging配置。python从字典加载配置可以参考[官方文档](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig)

python并没有yaml的相关包，需要第三方安装包，具体命令就是 pip3 install PyYaml，下面开始使用yaml。

config.yaml

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
version: 1
formatters:
    brief:
        format: "%(asctime)s - %(message)s"
    detail:
        format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
handlers:
    console:
        class: logging.StreamHandler
        formatter: detail
        level: INFO
        stream: ext://sys.stdout
    file_handler:
        class: logging.FileHandler
        formatter: detail
        level: DEBUG
        filename: debug.log
    error_handler:
        class: logging.FileHandler
        formatter: detail
        level: ERROR
        filename: error.log
loggers:
    main:
        level: DEBUG
        handlers: [file_handler, error_handler]
root:
    level: DEBUG
    handlers: [console]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

main.py

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging.config
import yaml
import os


def set_logging(default_path='config.yaml'):
    path = default_path
    if os.path.exists(path):
        with open(path) as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)


def main():
    set_logging()
    logger = logging.getLogger('main')
    logger.info('---Start info---')
    logger.debug('This is debug message')
    logger.error('Some error occurred')
    logger.info('---End info---')


if __name__ == '__main__':
    main()
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

程序从配置文件中读取了3个handler，其中2个写入文件和1个输出到控制台，输出结果如下

控制台:

```
2018-12-01 11:39:28,801 - main - INFO - ---Start info---
2018-12-01 11:39:28,801 - main - ERROR - Some error occurred
2018-12-01 11:39:28,802 - main - INFO - ---End info---
```

文件:

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# debug.log
2018-12-01 11:39:28,801 - main - INFO - ---Start info---
2018-12-01 11:39:28,801 - main - DEBUG - This is debug message
2018-12-01 11:39:28,801 - main - ERROR - Some error occurred
2018-12-01 11:39:28,802 - main - INFO - ---End info---

# error.log
2018-12-01 11:39:28,801 - main - ERROR - Some error occurred
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

注意: 上面的程序中，mainLogger只有两个文件handler，为什么会输出控制台呢？这是因为rootLogger是所有logger的祖先，程序运行过程中会通过根据logger的propagate属性决定是否把自己的record往父logger传，这个属性默认是True，换句话说，就是每一个record会至少被子logger和父logger的handler处理两次。在这个例子中，rootLogger有一个console的handler，所以会把信息输出到控制台，当我们不想消息依次往上传时，则可以把propagate属性设置为False。下面附上官方文档对propagate属性的说明链接[propagate](https://docs.python.org/3/library/logging.html?highlight=logging#logging.Logger)和handler处理的源码片段

```
c ``=` `self`      `# 这里的c是logger对象``found ``=` `0``while` `c:``   ``for` `hdlr ``in` `c.handlers:  ``# 这是循环依次处理每个logger的handler``     ``found ``=` `found ``+` `1``     ``if` `record.levelno >``=` `hdlr.level:``        ``hdlr.handle(record) ``# record是python的LogRecord对象``   ``if` `not` `c.propagate:    ``#如果该属性设置为True，则会依次往父logger传，直到root为止``     ``c ``=` `None`  `#break out``   ``else``:``     ``c ``=` `c.parent    　　
```

#### 9. 过滤器的使用[#](https://www.cnblogs.com/yscl/articles/10046479.html#4131141950)

logging模块原生的过滤器并没有过滤任何东西，所以当我们不满足只根据简单的分级来过滤信息，可以通过自己实现过滤器来完成复杂的功能。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import logging
import random
import sys


class ContextFilter(logging.Filter):

    def filter(self, record):
        if record.ip.split('.')[0] in ['123', '192']:　　# 此处把ip地址开头为123和192的过滤掉
            return False
        return True


if __name__ == '__main__':

    USERS = ['jim', 'fred', 'sheila', 'alex', 'hero']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1', '10.0.0.123']

    logger = logging.getLogger('__name__')
    logger.setLevel(logging.DEBUG)

    fmt = '%(asctime)s %(name)-8s %(levelname)s %(ip)-15s %(user)-8s %(message)s'
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    f = ContextFilter()
    logger.addFilter(f)

    for i in range(10):
        dic = {
            'ip': random.choice(IPS),
            'user': random.choice(USERS)
        }
        print(dic)
        logger.info('An info message', extra=dic)   # extra 是把字典里的属性添加到record中
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

控制台输出如下

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
{'user': 'jim', 'ip': '127.0.0.1'}
2018-12-01 12:04:12,217 __name__ INFO 127.0.0.1       jim      An info message
{'user': 'hero', 'ip': '123.231.231.123'}
{'user': 'hero', 'ip': '10.0.0.123'}
2018-12-01 12:04:12,217 __name__ INFO 10.0.0.123      hero     An info message
{'user': 'sheila', 'ip': '10.0.0.123'}
2018-12-01 12:04:12,217 __name__ INFO 10.0.0.123      sheila   An info message
{'user': 'fred', 'ip': '127.0.0.1'}
2018-12-01 12:04:12,217 __name__ INFO 127.0.0.1       fred     An info message
{'user': 'alex', 'ip': '123.231.231.123'}
{'user': 'hero', 'ip': '192.168.0.1'}
{'user': 'fred', 'ip': '192.168.0.1'}
{'user': 'alex', 'ip': '10.0.0.123'}
2018-12-01 12:04:12,217 __name__ INFO 10.0.0.123      alex     An info message
{'user': 'fred', 'ip': '10.0.0.123'}
2018-12-01 12:04:12,217 __name__ INFO 10.0.0.123      fred     An info message
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

可以看到随机生成的ip已经把ip开头为192和123的成功过滤掉了。

#### **参考:**[#](https://www.cnblogs.com/yscl/articles/10046479.html#1603880821)

[官方文档logging模块](https://docs.python.org/3/library/logging.html?highlight=logging#logrecord-objects)

[Python中logging模块的基本用法](https://cuiqingcai.com/6080.html)

[python标准模块](http://www.cnblogs.com/zhbzz2007/p/5943685.html)

[python root logger解密](https://www.jianshu.com/p/cad8a77762b3)

作者：[ yscl](http://blog.esofar.cn/)

出处：https://www.cnblogs.com/yscl/articles/10046479.html

版权：本站使用「[CC BY 4.0](https://creativecommons.org/licenses/by/4.0)」创作共享协议，转载请在文章明显位置注明作者及出处。

分类: [python常用模块](https://www.cnblogs.com/yscl/category/1497768.html)