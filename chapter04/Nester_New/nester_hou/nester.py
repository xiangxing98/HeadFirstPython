# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   nester.py
@Time    :   2020/09/01 18:22:09
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
import sys

def print_lol(the_list, indent=False, level=0, write_dest=sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1, write_dest)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t", end='',file=write_dest)
			print(each_item,file=write_dest)


