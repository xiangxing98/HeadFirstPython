"""
This can print all the intem in the list or in the list of list

Windows + R -> CMD

1. Change directory to module directry
cd /d F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter02\nester

2. Create distrabution tool
python setup.py sdist

writing manifest file 'MANIFEST'
creating nester-1.5.2
making hard links in nester-1.5.2...
hard linking nester.py -> nester-1.5.2
hard linking setup.py -> nester-1.5.2
Creating tar archive
removing 'nester-1.5.2' (and everything under it)

3. install
python setup.py install

running install
running build
running build_py
copying nester.py -> build\lib
running install_lib
copying build\lib\nester.py -> D:\ProgramFiles\Anaconda3\Lib\site-packages
byte-compiling D:\ProgramFiles\Anaconda3\Lib\site-packages\nester.py to nester.cpython-37.pyc
running install_egg_info
Writing D:\ProgramFiles\Anaconda3\Lib\site-packages\nester-1.5.2-py3.7.egg-info

4. Usage
import nester
nester.print_lol(movies)

5. http://pypi.python.org registration PyPI(Python Package Index)& Command line Confirn
python setup.py register
"""
import sys 
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
     """
     method 2, printtab is a bool value, if it is ture,in each sub list, it will print
     a TAB
     the_list: type:list
     indent: if this true, will print tab,决定着输出是否缩进
     level: 缩进的起始量,负数的话不缩进
     """
     for each_item in the_list:
          if (isinstance(each_item,list)):
               print_lol(each_item,indent,level+1,fh)
          else:
               if indent:
                    for tab_stop in range (level):
                         print('\t',end='',file=fh)
               print(each_item,file=fh)

      
