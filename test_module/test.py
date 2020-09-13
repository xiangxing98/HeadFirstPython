# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   test.py
@Time    :   2020/09/08 21:42:19
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# import io
# import sys
# 改变标准输出的默认编码
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def myFunction():
    print('Variable __name__ Current Value is: '+ __name__)
    print("Current Module Name is:", __name__)
    print('Execute Function myFunction over.\n')

def main():
    myFunction()
    print('Execute Function Main over.\n')

if __name__ == '__main__':
    print('__name__ == \'__main__\', Next Start Function Main.\n')
    main()

# __name__ == '__main__', Next Start Function Main.

# Variable __name__ Current Value is: __main__
# Current Module Name is: __main__
# Execute Function myFunction over.

# Execute Function Main over.

'''

# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd F:\\Github\\Python\\HeadFirstPython\\HeadFirstPython\\test_module\\test.py
python test.py

# Output:

'''