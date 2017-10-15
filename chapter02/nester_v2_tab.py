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

5. http://pypi.python.org registration & Command line Confirn
python setup.py register
"""
import sys 

# use level = 0 default value to compatibility v1.1
def print_lol_v2(the_list,level=0):
     """
     method 2, printtab is a bool value, if it is ture,in each sub list, it will print
     a TAB
     the_list: type:list
     level: 缩进的起始量,负数的话不缩进
     """
     for each_item in the_list:
          if (isinstance(each_item,list)):
               print_lol_v2(each_item, level + 1) # need 2 parameters
          else:
                for tab_stop in range (level):
                    print('\t',end='')
                print(each_item)

movies = [
     'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
     ['Graham Chapman',
      ['Michael Palin', 'John Cleese','Terry Gilliam','Eric Idle','Terry Jones']]]

print_lol_v2(movies, 0)
print("-----------------new line-----------------")
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# 	Graham Chapman
# 		Michael Palin
# 		John Cleese
# 		Terry Gilliam
# 		Eric Idle
# 		Terry Jones
# -----------------new line-----------------

print_lol_v2(movies)
print("-----------------new line-----------------")
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# 	Graham Chapman
# 		Michael Palin
# 		John Cleese
# 		Terry Gilliam
# 		Eric Idle
# 		Terry Jones
# -----------------new line-----------------

print_lol_v2(movies, 2)
# 2 tabs
# 		The Holy Grail
# 		1975
# 		Terry Jones&Terry Gilliam
# 		91
# 			Graham Chapman
# 				Michael Palin
# 				John Cleese
# 				Terry Gilliam
# 				Eric Idle
# 				Terry Jones

