"""
This can print all the intem in the list or in the list of list

1. Change directory to module directry
cd chapter02/nester/

2. Create distrabution tool
python setup.py sdist

3. install
python setup.py install

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

      
