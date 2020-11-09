# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   athletemodel.py
@Time    :   2020/09/15 22:59:54
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
import pickle
from athletelist import AthleteList


def get_coach_data(filename): #从文件中获取数据

     try:
          with open (filename) as f:
               data = f.readline()
               templ = data.strip().split(',')
               return (AthleteList(templ.pop(0),templ.pop(0),templ))
     except IOError as ioerr:
          print ('File Error: ' + str(ioerr))
          return (None)

def put_to_store(file_list):

     all_athletes = {}
     for each_f in file_list:
          ath = get_coach_data(each_f) #这里ath 返回的 athletelist 的对象(athletelist 是一个list)
          #all_athletes['Name'] = ath.name
          #all_athletes['DOB'] = ath.dob
          #all_athletes['Times']= ath
          all_athletes[ath.name] = ath #将ath name 作为键,将ath作为值
          
     try:
          with open ('athletes.pickle','wb') as ath_f:
               pickle.dump (all_athletes,ath_f)
     except IOError as ioerr:
          print('File Error(put_to_store): '+str(ioerr))
     return (all_athletes)

def get_from_store():

     all_athletes = {}
     try:
          with open ('athletes.pickle','rb') as ath_f:
               all_athletes = pickle.load(ath_f)
     except IOError as ioerr:
          print('File Error(get_from_store): '+str(ioerr))
          
     return (all_athletes)

"""
测试代码
files = ['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data = put_to_store(files)#data 是一个字典
print(data)
for each_ath in data:
     #print(data[each_ath].name + ' ' +data[each_ath].dob )
     print(data[each_ath].name)
"""
