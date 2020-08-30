# Head First Python Learning Notes

Head First 系列的书籍一直饱受赞誉，这本也不例外。Head First Python主要讲述了Python 3的基础语法知识以及如何使用Python快速地进行Web、手机上的开发。

下面是该书每章结束部分的知识摘要：



## 第一章 初始Python：人人都爱列表(Lists)

1. 从命令行或者IDLE里都可以运行Python 3；
2. 标识符是指代数据对象的名称，它本身并没有“类型”，但是它所指代的数据对象拥有类型；
3. 内置函数print()可以在屏幕上显示消息；
4. Python中的列表list是用中括号包住的以逗号分隔的数据集合；
5. list和数组非常相似；
6. list既可以使用内置函数，也可以使用针对列表本身的函数；
7. list的大小按需自动伸缩。数据使用的所有内存都由Python管理；
8. len()内置函数用来计算数据对象的长度或是某个集合（如list）内条目的数量；
9. for循环可以帮助遍历list，它用起来通常比等价的while循环更方便；
10. if...else...语句帮助在代码中做出不同的选择；
11. isinstance()内置函数可用来检测标识符指代的数据对象是否为指定类型；
12. 使用def定义自定义函数。

## 第二章 分享代码：函数模块

1. 模块是包含Python代码的文本文件；
2. 分发工具(distribution utilities)帮助您将模块变为可共享的包；
3. setup.py程序提供了关于模块的元数据，他可以用于生成，安装和上传分发包；
4. 使用import语句将模块导入到其他程序中；
5. Python中每个模块都提供了自己的命名空间。它在使用module.function()形式调用时用以限定模块内的函数。
6. 使用形如from module import function的import语句可以将模块内特定函数导入当前命名空间；
7. 使用#可以将一行代码变为注释或者为程序添加一条精短且在一行内的注释；
8. 内置函数拥有自己的命名空间，叫做__builtins__，它会自动包含进每个Python程序中。
9. range()内置函数可以和for用在一起进行固定次数的遍历；
10. 在print()内置函数结尾包含end=''可以关掉输出时自动添加的换行符；
11. 如果为函数参数提供默认值，那么它们就为成为可选参数。

## 第三章 文件和异常：处理错误

1. 使用open()内置函数打开磁盘文件并创建一个迭代器来每次从文件中读取一行数据；
2. readline()方法从一个打开的文件中读取一行数据；
3. seek()方法可以将文件重新定位到开头；
4. close()方法关闭上一次打开的文件；
5. split()方法将一个字符串分为许多份组成的列表；
6. Python中不可改变的常量list叫做tuple。一旦列表数据复制给一个tuple之后，tuple中的数据将不能再被改变。Tuple是不能变的(immutable);
7. 当数据与期望的格式有出入时，会产生ValueError；
8. 当数据没法被正确访问时（例如数据文件可能已经移动过或者重命名过），会产生IOError；
9. help()内置函数提供在IDLE shell中访问Python文档；
10. find()方法可以在一个字符串中查找特定子串；
11. not关键字用来否定一个条件；
12. try/except语句提供了异常处理机制，可以保护那些可能导致运行时错误的代码段；
13. pass语句是Python中的空语句，它什么都不做。

## 第四章 持久化：将数据存成文件

1. strip()方法移除字符串首尾空白字符；
2. print()内置函数中的file参数可以控制data是读入或是写出；
3. 不管try/except语句中是否有异常发生，finally的代码段总是会被执行；
4. 异常对象会传入到except代码段，并且可以使用as关键字将其赋值给一个标识符；
5. str()内置函数可以用来访问任何数据对象的字符串表示，前提是该数据对象支持该转换；
6. locals()内置函数返回当前作用范围内的变量集合；
7. in操作符可用于测试成员包含关系；
8. "+"操作符应用于两个字符串时会得到它们的串联结果，而应用于数字时会得到它们的相加和；
9. with语句即使在异常发生的情况下，也会自动去关闭所有打开的文件。with语句同样可以使用as关键字；
10. sys.stdout是Python中的标准输出，它位于标准库中的sys模块；
11. 标准库pickle模块可以让轻松高效地保存Python数据对象到磁盘和从磁盘恢复Python数据对象；
12. pickle.dump()函数将数据存盘；
13. pickle.load()函数从磁盘恢复数据。

## 第五章 理解数据：让数据动起来

1. sort()方法原地排序列表；
2. sorted()内置函数通过复制排序的方式可以对大多数数据结构进行排序；
3. 传入sort()或sorted的参数reverse=True可以将数据进行降序排序；
4. 形如下面的代码段：
new_l = []
for t in old_l:
    new_l.append(len(t))
可以重写为列表表达式形式：[len(t) for t in old_l]
5. 使用切片从list中获取多个数据条目，如：my_lis[3:6]会从索引3的位置访问到索引6的位置，不包含6。
6. 使用set()工厂方法创建一个集合

## 第六章 自定义数据对象：围绕数据编码

1. 使用dict()工厂函数或使用{}来创建一个空的dictionary；
2. 访问一个叫做person的dictionary中Name键所对应的值，可是使用熟悉的中括号记法：person['Name'];
3. 同list和set类似，Python的dictionary数据结构也会随着新元素的加入动态的增长；
4. 填充dictionary的方法有：new_d = {}或new_d = dict()，然后使用d['Name'] = 'Eric Idle'；或者直接用一句话new_d = {'Name': 'Eric Idle'};
5. class关键字用来定义类；
6. 类中方法的定义与函数非常相像，都使用def关键字；
7. 类中属性就如同对象实例内部的变量；
8. __init__()方法可以定义在类中用作实例化对象实例；
9. 类中定义的每个方法都必须提供self作为第一个参数；
10. 类中的每个属性都必须使用self为前缀，以使得数据能与实例关联在一起；
11. 既可以从头开始创建类也可以从Python内置或自定义类中继承；
12. 类可以被放入Python模块并上传到PyPI。

## 第七章 Web开发：信息汇总

1. MVC模式(Model-View-Controller)用一种可维护的方式帮助设计和构建一个Web应用；
2. model存储Web应用中的数据；
3. view显示Web应用的用户界面；
4. controller使用编程逻辑将所有部分连接在一起；
5. 标准库string模块中有一个类叫做Template，它支持简单的字符串替换；
6. 标准库http.server模块可以用来在Python中创建一个简单的Web服务器；
7. 标准库cgi模块提供编写CGI脚本的支持；
8. 标准库glob模块处理文件列表非常好用；
9. 在Linux和Mac OS X上为可执行文件执行chmod+x命令；
10. 标准库cgitb模块在激活时可以在浏览器中看到CGI的编码错误；
11. 使用cgitb.enable()可以在CGI代码中打开CGI跟踪；
12. 使用cgi.FieldStorage()可以访问发送到Web服务器请求部分的数据。

## 第八章 移动应用开发：小型设备

1. json库模块可以将Python内置类型转为JSON数据交换格式；
2. 使用json.dumps()可以创建Python类型的字符串版本；
3. 使用json.loads()从JSON字符串中创建Python类型；
4. 使用JSON发布数据需要制定Content-Type为application/json;
5. Python 2中的urllib和urllib2可以用与发送编码后的数据给Web服务器（使用urlencode和urlopen函数）；
6. sys模块提供了sys.stdin, sys.stdout和sys.stderr输入流。

## 第九章 管理数据：处理输入

1. 标准库cgi模块中的fieldStorage()方法可以访问CGI脚本中发送给Web服务器的数据；
2. 标准库os中包含的environ字典，提供了对环境变量设置的轻松访问；
3. SQLLite数据库系统在Python中作为sqlite3标准库存在；
4. connect()方法建立与数据库文件的连接；
5. cursor()方法通过一个已有连接与数据库进行通信；
6. execute()方法通过一个已有游标向数据库发送SQL查询；
7. commit()方法对数据库做出永久性的改变；
8. rollback()方法取消任何针对数据的待定改动；
9. close()方法会关闭数据库的已有连接；
10. Python代码中的"?"占位符可以参数化SQL语句。

## 第十章 扩展Web应用：变得真实

1. 每个App Engine Web应用都必须有一个叫做app.yaml的配置文件；
2. 使用GAE启动器启动、停止、监控、测试、上传以及部署Web应用；
3. App Engine的模板技术基于Django项目；
4. App Engine也可以使用Django表单验证框架；
5. 使用self.response对象构造一个GAE Web应答；
6. 使用self.request对象在GAE Web应用中访问表单数据；
7. 当应答GET请求时，可以子啊get()方法中实现需要的功能；
8. 当应答POST请求时，在post()方法中实现需要的功能；
9. 使用put()方法将数据存储到App Engine datastore中。

## 第十一章 处理复杂数据

1. input()内置函数提示并接受来自用户的输入；
2. 如果发现在使用的是Python2，可以使用原生的_input()函数来取代input()函数；
3. 使用Python内置的列表、集合及字典构建复杂数据结构；
4. 标准库中的time模块，有大量函数可以用来转换不同的时间格式。

## 书中没有谈到的10件重要的事

### 1. 使用专业的IDE

书中推荐的是WingWare Python IDE。我一直在用的是Eclipse + PyDev

### 2. 积极面对作用域

使用global关键字可以强制将全局变量放入当前作用域

### 3. 测试

书中提到了两个用于测试的框架，一个是Python中的unittest模块；另一个也是标准库中的doctest

### 4. 高级语言特性

匿名函数、生成器、自定义异常、函数修饰符、元数据类等

### 5. 正则表达式

### 6. 更多的Web框架

Django、Zope、TurboGears、Web2py、Pylons等

### 7. 对象关系映射(ORM)以及NoSQL

ORM工具：SQL Alchemy
NoSQL数据库：CouchDB和MongoDB

### 8. 用户界面编程

Python内置的跨平台的GUI构建工具集——tkinter(Tk Interface)。
其他的GUI编程技术有：PyGTK，PyKDE，WxPython和PyQT等。

### 9. 避免使用多线程

Python中的全局解释锁限定Python只能运行单个解释进程，即使多核情况下也不行

### 10. 书籍推荐

Dive into Python 3
Python Essential Reference
Programming in Python
Learning Python
...



# Head First  Python Jupyter Notebook

1. Head First Python Chapter 01-Learning Notes.ipynb
2. Head First Python Chapter 02-Learning Notes.ipynb

Table of contents
Dedication
Advance Praise for Head First Python, Second Edition
Praise for the first edition
Praise for other Head First books
Praise for other Head First books

Author of Head First Python, 2nd Edition
How to use this Book: Intro
Who Is This Book For?
Who should probably back away from this book?
We Know What You’re Thinking
We know what your brain is thinking
Metacognition: Thinking About Thinking
Here’s What WE Did:
Here’s what YOU can do to bend your brain into submission
Read Me, 1 of 2
Read Me, 2 of 2
The Technical Review Team
Acknowledgments and Thanks
O’Reilly Safari
1. The Basics: Getting Started Quickly
Breaking with Tradition
Starting with a meatier example
Jump Right In
Python’s IDLE is all you need to get going
Understanding IDLE’s Windows
What Happens Next...
Press F5 to Run Your Code
Code Runs Immediately
Executing Code, One Statement at a Time
Let’s be the Python interpreter
Functions + Modules = The Standard Library
Batteries Included
Data Structures Come Built-in
Python variables are dynamically assigned
Invoking Methods Obtains Results
Invoking built-in module functionality
Deciding When to Run Blocks of Code
What Happened to My Curly Braces?
A colon introduces an indented suite of code
What “else” Can You Have with “if”?
Suites Can Contain Embedded Suites
What We Already Know
Extending Our Program to Do More
What we need to do:
What’s the Best Approach to Solving This Problem?
Both approaches work with Python
Returning to the Python Shell
Experimenting at the Shell
Iterating Over a Sequence of Objects
Iterating a Specific Number of Times
Applying the Outcome of Task #1 to Our Code
Indent Suites with Format...Indent Region
Arranging to Pause Execution
Importation Confusion
Generating Random Integers with Python
Asking the Interpreter for Help
Reviewing Our Experiments
Updating What We Already Know
A Few Lines of Code Do a Lot
Coding a Serious Business Application
Dealing with all that beer...
Python Code Is Easy to Read
Is Indentation Driving You Crazy?
Getting back to the beer song code
Asking the Interpreter for Help on a Function
Starting, stopping, and stepping
Experimenting with Ranges
Don’t Forget to Try the Beer Song Code
Wrapping up what you already know
With all the beer gone, what’s next?
Chapter 1’s Code
2. List Data: Working with Ordered Data
Numbers, Strings...and Objects
Numbers
Strings
Objects
“Everything Is an Object”
But...what does all this actually mean?
Meet the Four Built-in Data Structures
Ordered Collections Are Mutable/Immutable
An Unordered Data Structure: Dictionary
A Data Structure That Avoids Duplicates: Set
The 80/20 data structure rule of thumb
A List Is an Ordered Collection of Objects
How to spot a list in code
Creating Lists Literally
Putting Lists to Work
Working with lists
Is one object inside another? Check with “in”
Use Your Editor When Working on More Than a Few Lines of Code
Don’t forget: press F5 to run your program
“Growing” a List at Runtime
Checking for Membership with “in”
Is the object “in” or “not in”?
It’s Time to Update Our Code
Removing Objects from a List
Popping Objects Off a List
Extending a List with Objects
Inserting an Object into a List
What About Using Square Brackets?
What Happened to “plist”?
Lists: What We Know
What Looks Like a Copy, But Isn’t
How to Copy a Data Structure
Square Brackets Are Everywhere
Lists: Updating What We Already Know
Lists Extend the Square Bracket Notation
Lists Understand Start, Stop, and Step
You can put start, stop, and step inside square brackets
List Slices in Action
Starting and Stopping with Lists
Stepping with Lists
Slices are everywhere
Putting Slices to Work on Lists
Converting “Don’t panic!” to “on tap”
Putting Slices to Work on Lists, Continued
Which Is Better? It Depends...
Slicing a List Is Nondestructive
So...which is better?
Python’s “for” Loop Understands Lists
Understanding marvin.py’s code
Python’s “for” Loop Understands Slices
Marvin’s Slices in Detail
Lists: Updating What We Know
What’s Wrong with Lists?
When Not to Use Lists
Chapter 2’s Code, 1 of 2
Chapter 2’s Code, 2 of 2
3. Structured Data: Working with Structured Data
A Dictionary Stores Key/Value Pairs
Make Dictionaries Easy to Read
How to Spot a Dictionary in Code
What happened to the insertion order?
Insertion Order Is NOT Maintained
Dictionaries understand square brackets
Value Lookup with Square Brackets
Dictionary lookup is fast!
Working with Dictionaries at Runtime
Recap: Displaying Found Vowels (Lists)
How Can a Dictionary Help Here?
Selecting a Frequency Count Data Structure
Updating a Frequency Counter
Updating a Frequency Counter, v2.0
Iterating Over a Dictionary
Iterating Over Keys and Values
Dictionaries: What We Already Know
Specifying the ordering of a dictionary on output
Iterating Over a Dictionary with “items”
Just How Dynamic Are Dictionaries?
Dictionary keys must be initialized
Avoiding KeyErrors at Runtime
Checking for Membership with “in”
Ensuring Initialization Before Use
Substituting “not in” for “in”
Putting the “setdefault” Method to Work
Dictionaries: updating what we already know
Aren’t Dictionaries (and Lists) Enough?
Sets Don’t Allow Duplicates
Spotting sets in your code
Creating Sets Efficiently
Creating sets from sequences
Taking Advantage of Set Methods
union Works by Combining Sets
What happened to the loop code?
difference Tells You What’s Not Shared
intersection Reports on Commonality
Sets: What You Already Know
Using a set was the perfect choice here...
Making the Case for Tuples
How to spot a tuple in code
Tuples Are Immutable
Watch Out for Single-Object Tuples
Combining the Built-in Data Structures
Storing a Table of Data
A Dictionary Containing a Dictionary
A Dictionary of Dictionaries (a.k.a. a Table)
Pretty-Printing Complex Data Structures
Visualizing Complex Data Structures
Accessing a Complex Data Structure’s Data
Data Is As Complex As You Make It
Chapter 3’s Code, 1 of 2
Chapter 3’s Code, 2 of 2
4. Code Reuse: Functions and Modules
Reusing Code with Functions
Introducing Functions
What About Type Information?
Naming a Chunk of Code with “def”
Invoking Your Function
Edit your function in an editor, not at the prompt
Use IDLE’s Editor to Make Changes
What’s the Deal with All Those Strings?
Understanding the string quote characters
Follow Best Practice As Per the PEPs
Functions Can Accept Arguments
Functions Return a Result
Returning One Value
Returning More Than One Value
What’s the deal with “set()”?
Recalling the Built-in Data Structures
Use Annotations to Improve Your Docs
Why Use Function Annotations?
Functions: What We Know Already
Making a Generically Useful Function
Creating Another Function, 1 of 3
Creating Another Function, 2 of 3
Creating Another Function, 3 of 3
Specifying Default Values for Arguments
Positional Versus Keyword Assignment
Updating What We Know About Functions
Functions Beget Modules
Creating modules couldn’t be easier, however...
How Are Modules Found?
Running Python from the Command Line
Not Found Modules Produce ImportErrors
ImportErrors Occur No Matter the Platform
Getting a Module into Site-packages
Using “setuptools” to install into site-packages
Creating the Required Setup Files
Creating the Distribution File
Creating a distribution file on Windows
Distribution Files on UNIX-like OSes
Installing Packages with “pip”
Step 3 on Windows
Step 3 on UNIX-like OSes
Modules: What We Know Already
Giving your code away (a.k.a. sharing)
Demonstrating Call-by-Value Semantics
Demonstrating Call-by-Reference Semantics
Can I Test for PEP 8 Compliance?
Getting Ready to Check PEP 8 Compliance
Recalling our code
Installing pytest and the pep8 plug-in
Install the Testing Developer Tools
How PEP 8–Compliant Is Our Code?
Understanding the Failure Messages
Confirming PEP 8 Compliance
Conformance to PEP 8 is a good thing
Chapter 4’s Code
5. Building a Webapp: Getting Real
Python: What You Already Know
Let’s Build Something
What Do We Want Our Webapp to Do?
What Happens on the Web Server?
What do we need to get going?
Let’s Install Flask
Install Flask from the command-line with pip
How Does Flask Work?
Check that Flask is installed and working
Run Flask from your OS command line
Running Your Flask Webapp for the First Time
Here’s What Happened (Line by Line)
Creating a Flask Webapp Object
Decorating a Function with a URL
Running Your Webapp’s Behavior(s)
Exposing Functionalit y to the Web
Recall What We’re Trying to Build
Here’s the plan
Building the HTML Form
But...what if you’re new to all this HTML stuff?
Create the HTML, then send it to the browser
Templates Relate to Web Pages
Rendering Templates from Flask
Displaying the Webapp’s HTML Form
Preparing to Run the Template Code
We’re Ready for a Test Run
Understanding HTTP Status Codes
Handling Posted Data
Refining the Edit/Stop/Start/Test Cycle
Accessing HTML Form Data with Flask
Using Request Data in Your Webapp
Automatic Reloads
Producing the Results As HTML
Calculating the Data We Need
Adding a Finishing Touch
Redirect to Avoid Unwanted Errors
Functions Can Have Multiple URLs
Updating What We Know
Is that all there is to this chapter?
Preparing Your Webapp for the Cloud
Exploiting Dunder Name Dunder Main
Deploying to PythonAnywhere (well... almost)
Chapter 5’s Code
6. Storing and Manipulating Data: Where to Put Your Data
Doing Something with Your Webapp’s Data
Python Supports Open, Process, Close
Reading Data from an Existing File
A Better Open, Process, Close: “with”
The “with” statement manages context
Invoking the logging function
A Quick Review
Take your webapp for a spin...
Data is logged (behind the scenes)
View the Log Through Your Webapp
Where to start when things go wrong with your output
Examine the Raw Data with View Source
It’s Time to Escape (Your Data)
Viewing the Entire Log in Your Webapp
Learning More About the Request Object
What’s all this, then?
Logging Specific Web Request Attributes
Log a Single Line of Delimited Data
One Final Change to Our Logging Code
From Raw Data to Readable Output
Does This Remind You of Anything?
Use a Dict of Dicts...or Something Else?
Take a closer look at the logged data
What’s Joined Together Can Be Split Apart
Getting to a list of lists from a list of strings
When Should the Conversion Occur?
Processing Data: What We Already Know
Take a closer look at the output
Generate Readable Output With HTML
Embed Display Logic in Your Template
Producing Readable Output with Jinja2
The Current State of Our Webapp Code
Asking Questions of Your Data
Chapter 6’s Code
7. Using a Database: Putting Python’s DB-API to Use
Database-Enabling Your Webapp
Task 1: Install the MySQL Server
Introducing Python’s DB-API
Task 2: Install a MySQL Database Driver for Python
Install MySQL-Connector/Python
Task 3: Create Our Webapp’s Database and Tables
Decide on a Structure for Your Log Data
Confirm Your Table Is Ready for Data
Task 4: Create Code to Work with Our Webapp’s Database and Tables
Storing Data Is Only Half the Battle
This new function is a big change
How Best to Reuse Your Database Code?
Consider What You’re Trying to Reuse
What About That Import?
Be careful when positioning your import statements
Consider What You’re Trying to Do
You’ve Seen This Pattern Before
The Bad News Isn’t Really All That Bad
Chapter 7’s Code
8. A Little Bit of Class: Abstracting Behavior and State
Hooking into the “with” Statement
An Object-Oriented Primer
A class bundles behavior and state
Classes have methods and attributes
Creating Objects from Classes
Objects Share Behavior but Not State
Defining what we want CountFromBy to do
Doing More with CountFromBy
It’s Worth Repeating Ourselves: Objects Share Behavior but Not State
Invoking a Method: Understand the Details
Method Invocation: What Actually Happens
Adding a Method to a Class
Are You Serious About “self”?
The Importance of “self”
Coping with Scoping
Prefix Your Attribute Names with “self”
Initialize (Attribute) Values Before Use
Dunder “init” Initializes Attributes
Initializing Attributes with Dunder “init”
Pass any amount of argument data to dunder “init”
What have we learned from this Test Drive?
Understanding CountFromBy’s Representation
Defining CountFromBy’s Representation
Providing Sensible Defaults for CountFromBy
Classes: What We Know
Chapter 8’s Code
9. The Context Management Protocol: Hooking into Python’s with Statement
What’s the Best Way to Share Our Webapp’s Database Code?
Consider What You’re Trying to Do, Revisited
How best to create a context manager?
Managing Context with Methods
Dunder “enter” performs setup
Dunder “exit” does teardown
(As you know) dunder “init” initializes
You’ve Already Seen a Context Manager in Action
What’s required from you
Create a New Context Manager Class
Initialize the Class with the Database Config
Your context manager begins to take shape
Perform Setup with Dunder “enter”
Don’t forget to prefix all attributes with “self”
Perform Teardown with Dunder “exit”
Your context manager is re ady for testing
There’s not much code here, is there?
Reconsidering Your Webapp Code, 1 of 2
Reconsidering Your Webapp Code, 2 of 2
Recalling the “log_request” Function
Amending the “log_request” Function
Recalling the “view_the_log” Function
It’s Not Just the Code That Changes
Amending the “view_the_log” Function
Here’s the SQL query you’ll need
It’s nearly time for one last Test Drive
All That Remains...
Answering the Data Questions
How many requests have been responded to?
What’s the most common list of letters?
Which IP addresses are the requests coming from?
Which browser is being used the most?
Chapter 9’s Code, 1 of 2
Chapter 9’s Code, 2 of 2
10. Function Decorators: Wrapping Functions
Your Webapp Is Working Well, But...
Only authenticated users gain access
The Web Is Stateless
HTTP is to blame...
Your Web Server (Not Your Computer) Runs Your Code
It’s Time for a Bit of a Session
Flask’s Session Technology Adds State
Dictionary Lookup Retrieves State
Time for a Test Drive?
Managing Logins with Sessions
Let’s Do Login
Amend the webapp’s code to handle logins
Let’s Do Logout and Status Checking
Amend the webapp’s code once more
Why Not Check for False?
Can We Now Restrict Access to URLs?
Copy-and-Paste Is Rarely a Good Idea
Put shared code into its own function
Creating a Function Helps, But...
You’ve Been Using Decorators All Along
Pass a Function to a Function
Functions can take a function as an argument
Invoking a Passed Function
Functions Can Be Nested Inside Functions
When would you ever use this?
Return a Function from a Function
Accepting a List of Arguments
Use * to accept an arbitrary list of arguments
Processing a List of Arguments
* works on the way in, too
Accepting a Dictionary of Arguments
Use ** to accept arbitrary keyword arguments
Processing a Dictionary of Arguments
** works on the way in, too
Accepting Any Number and Type of Function Arguments
A Recipe for Creating a Function Decorator
Recap: We Need to Restrict Access to Certain URLs
Creating a Function Decorator
That’s almost too easy, isn’t it?
Can you see why the nested function is called “wrapper”?
The Final Step: Handling Arguments
We’re done...or are we?
Your Decorator in All Its Glory
Putting Your Decorator to Work
The Beauty of Decorators
Creating More Decorators
Back to Restricting Access to /viewlog
What’s Next?
Chapter 10’s Code, 1 of 2
Chapter 10’s Code, 2 of 2
11. Exception Handling: What to Do When Things Go Wrong
Databases Aren’t Always Available
Web Attacks Are a Real Pain
Input-Output Is (Sometimes) Slow
Your Function Calls Can Fail
Considering the Identified Problems
1. Your database connection fails
2. Your application is subjected to an attack
3. Your code takes a long time to execute
4. Your function call fails
Always Try to Execute Error-Prone Code
Catching an Error Is Not Enough
There can be more than one exception raised...
try Once, but except Many Times
A Lot of Things Can Go Wrong
The Catch-All Exception Handler
Haven’t We Just Lost Something?
Learning About Exceptions from “sys”
The Catch-All Exception Handler, Revisited
Getting Back to Our Webapp Code
Silently Handling Exceptions
Handling Other Database Errors
Does “More Errors” Mean “More excepts”?
Avoid Tightly Coupled Code
The DBcm Module, Revisited
Creating Custom Exceptions
The empty class isn’t quite empty...
What Else Can Go Wrong with “DBcm”?
Creating More Custom Exceptions
Are Your Database Credentials Correct?
Handling SQLError Is Different
Be Careful with Code Positioning
Raising an SQLError
A Quick Recap: Adding Robustness
What happens if something takes a long time?
How to Deal with Wait? It Depends...
Chapter 11’s Code, 1 of 3
Chapter 11’s Code, 2 of 3
Chapter 11’s Code, 3 of 3
12. 11¾ A Little Bit of Threading: Dealing with Waiting
Waiting: What to Do?
How Are You Querying Your Database?
Database INSERTs and SELECTs Are Different
Doing More Than One Thing at Once
Concurrent code: you have options
Don’t Get Bummed Out: Use Threads
First Things First: Don’t Panic
Don’t Get Bummed Out: Flask Can Help
Is Your Webapp Robust Now?
Chapter 11¾’s Code, 1 of 2
Chapter 11¾’s Code, 2 of 2
13. Advanced Iteration: Looping Like Crazy
Bahamas Buzzers Have Places to Go
Reading CSV Data As Lists
Reading CSV Data As Dictionaries
Let’s Back Up a Little Bit
Stripping, Then Splitting, Your Raw Data
Be Careful When Chaining Method Calls
Transforming Data into the Format You Need
Transforming into a Dictionary Of Lists
Think about the data wrangling that’s needed here...
Let’s Do the Basic Conversions
Did You Spot the Pattern in Your Code?
Spotting the Pattern with Lists
Converting Patterns into Comprehensions
Take a Closer Look at the Comprehension
What’s the Big Deal?
Comprehensions aren’t just for lists
Specifying a Dictionary Comprehension
Extend Comprehensions with Filters
Recall What You Set Out to Do
Deal with Complexity the Python Way
Extract a Single Destination’s Flight Times
Extract Flight Times for All Destinations
That Feeling You Get...
The Set Comprehension in Action
How to Spot a Comprehension
What About “Tuple Comprehensions”?
Parentheses Around Code == Generator
Generators produce data items one at a time...
Using a Listcomp to Process URLs
Using a Generator to Process URLs
Using a Generator: What Just Happened?
Define What Your Function Needs to Do
Yield to the Power of Generator Functions
Tracing Your Generator Function, 1 of 2
Tracing Your Generator Function, 2 of 2
Concluding Remarks
One Final Question
Chapter 12’s Code
It’s Time to Go…
You’re on your way!
A. Installation: Installing Python
Install Python 3 on Windows
Download, then install
Check Python 3 on Windows
It’s Python 3 on Windows, sort of...
Add to Python 3 on Windows
Install Python 3 on Mac OS X (macOS)
Using a package manager
Check and Configure Python 3 on Mac OS X
The Python 3 folder on Mac OS X
You’re ready to run on Mac OS X
Install Python 3 on Linux
B. Pythonanywhere: Deploying Your Webapp
Step 0: A Little Prep
Step 1: Sign Up for PythonAnywhere
Step 2: Upload Your Files to the Cloud
Step 3: Extract and Install Your Code
Step 4: Create a Starter Webapp, 1 of 2
Step 4: Create a Starter Webapp, 2 of 2
Step 5: Configure Your Webapp
Step 6: Take Your Cloud-Based Webapp for a Spin!
C. Top Ten Things we Didn’t Cover: There’s Always More to Learn
1. What About Python 2?
2. Virtual Programming Environments
3. More on Object Orientation
4. Formats for Strings and the Like
5. Getting Things Sorted
6. More from the Standard Library
collections
itertools
functools
7. Running Your Code Concurrently
New keywords: async and await
8. GUIs w ith Tkinter (and Fun w ith Turtles)
9. It’s Not Over ’Til It’s Tested
10. Debug, Debug, Debug
D. Top Ten Projects not Covered: Even More Tools, Libraries, and Modules
1. Alternatives to >>>
2. Alternatives to IDLE
What does Paul use?
3. Jupyter Notebook: The Web-Based IDE
4. Doing Data Science
5. Web Development Technologies
But wait, there’s more
6. Working with Web Data
Scrape that web data!
7. More Data Sources
There’s more to querying data than SQL
8. Programming Tools
More help with testing, too
9. Kivy: Our Pick for “Coolest Project Ever”
10. Alternative Implementations
E. Getting Involved: The Python Community
BDFL: Benevolent Dictator for Life
PSF: The Python Sof t ware Foundation
PyCon: The Python Conference
A Tolerant Community: Respect for Diversit
Come for the language, stay for the community
Python Podcasts
Python Newsletters
The Zen of Python
Which Book Should I Read Next?
Our Favorite Python Books
Index
About the Author
Copyright