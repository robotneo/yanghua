#! /usr/bin/env python
# -*- coding: utf-8 -*-

#记录生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

constellation_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', 
u'巨蟹座', u'狮子座', u'处女座', u'天秤座',u'天蝎座', u'射手座')


constellation_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                        (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

int_month = int(input('请输入月份: '))
int_day = int(input('请输入日期: '))

for zd_num in range(len(constellation_days)):
    if constellation_days[zd_num] >= (int_month, int_day):
        print(constellation_name[zd_num])
        break
    elif int_month == 12 and int_day >23:
        print(constellation_name[0])
        break