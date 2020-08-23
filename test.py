# -*- encoding: utf-8 -*- 
# !/usr/bin/env python
'''
@File    :   test.py
@Time    :   2020/08/23 11:16:38
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
@File    :   test.py
'''

# here put the import lib
import sys

if __name__ == "__main__":
    print("hello.")
    for i in range(0, len(sys.argv), 1):
        print("Parameter%d: " % i, sys.argv[i], sep = ' ')
    print("Will Exit.")
    sys.exit(0)
"""
hello.
Parameter0:  e:\Github\Python\HeadFirstPython\HeadFirstPython\test.py
Parameter1:  1st_param
Parameter2:  2nd_param
Will Exit.
"""

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd F:\Github\Python\HeadFirstPython\HeadFirstPython\test.py
python test.py

# Output:

'''
