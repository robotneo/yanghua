#! /usr/bin/env python
# -*- coding: utf-8 -*-

#记录生肖，根据年份来判断生肖
""" chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

constellation_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', 
u'巨蟹座', u'狮子座', u'处女座', u'天秤座',u'天蝎座', u'射手座')


constellation_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                        (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (4, 20)
constellation_to_zodiac = filter(lambda x: x<=(month, day), constellation_days)

constellation_to_zodiac_len = len(list(constellation_to_zodiac)) % 12
print(constellation_name[constellation_to_zodiac_len])
#print(chinese_zodiac[0:4])
#print(chinese_zodiac[-10])

year = int(input("请输入年份: "))
#print(type(year))
zodiacindex = year % 12
print(zodiacindex)
print(type(zodiacindex))
print(chinese_zodiac[zodiacindex]) """

listdemo = [u"郭靖", u"黄蓉", u"独孤求败", u"乔峰", u"虚竹", u"段誉", u"张无忌"]

print(listdemo[3])
print(listdemo[1:4])