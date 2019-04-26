#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
dict1 = {}
dict2 = {'x': 1, 'y': 2}
dict2['z'] = 3

print(type(dict1))
print(dict2)


chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
constellation_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', 
u'巨蟹座', u'狮子座', u'处女座', u'天秤座',u'天蝎座', u'射手座')

constellation_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                        (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
#初始化
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in constellation_name:
    z_num[i] = 0


while True:

    int_year = int(input('请输入年份: '))
    int_month = int(input('请输入月份: '))
    int_day = int(input('请输入日期: ')) 

    n = 0
    while constellation_days[n] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
        n += 1
    #输入生肖和星座
    print(constellation_name[n])
    print('%s 年的生肖是 %s' %(int_year, chinese_zodiac[int_year % 12]))

    cz_num[chinese_zodiac[int_year % 12]] += 1
    z_num[constellation_name[n]] += 1

    #输出生肖和星座的统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' %(each_key, cz_num[each_key]))
    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' %(each_key, z_num[each_key]))
'''

person_class = (u"成年", u"未成年")

count = {}

for i in person_class:
    count[i] = 0

while True:
    age = int(input('请输入年龄'))
    if age >= 18:
        count[person_class[0]] += 1
    elif age < 18:
        count[person_class[1]] += 1
    elif str(age) == " ":
        break
    print('统计数据：', count)
