"""This is the "nester.py" module and it provides one function called
print_lol() which prints lists that may or may not include nested lists"""

def print_lol(the_list):
        """This function takes a positional argument called "the_list", which is any
        Python list (of, possibly, nested lists). Each data item in the provided list
        is (recursively printed to the screen on its own line"""
        for item in the_list:
                if isinstance(item,list):
                        print_lol(item)
                else:
                        print(item)
'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd F:\Github\Python\HeadFirstPython\HeadFirstPython\chapter02\nester.py
python nester.py

# Output:

'''