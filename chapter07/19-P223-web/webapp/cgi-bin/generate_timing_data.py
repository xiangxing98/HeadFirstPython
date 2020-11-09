# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   generate_timing_data.py
@Time    :   2020/09/15 22:21:09
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

import cgi
import cgitb #开启浏览器追踪 cig 信息

import athletemodel
import YATE

cgitb.enable()#cgitb #开启浏览器追踪 cig 信息
athletes = athletemodel.get_from_store()#从pickle获取信息
form_data = cgi.FieldStorage()#获取请求的form的内容
athlete_name = form_data['which_athlete'].value#从内容中得到请求控件name 为:which_athlete的值
                         
print(YATE.start_response())
print(YATE.include_header('Timing Data'))
print(YATE.header('Athlete:'+athlete_name+' ,DOB: '
                  +athletes[athlete_name].dob+'.'))
print(YATE.para('The top times for this athlete are:'))
print(YATE.u_list(athletes[athlete_name].top3))#这里需要在top3方法那加入@property将类方法表现得像个类属性
print(YATE.include_footer({'Home':'/index.html',
                           'Select another athlete':'generate_list.py'}))
