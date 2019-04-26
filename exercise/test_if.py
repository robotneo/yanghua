#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
a = 'abc'
if a == 'abc':
    print("a和b相等")
else:
    print("a和b不相等")

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input('请输入出生年份: '))
if (chinese_zodiac[year % 12]) == '猪':
    print('狗年运势。。。')
else:
    print('其他年运势')

for cz in chinese_zodiac:
    print(cz)

for i in range(1, 14):
    print(i)

for year in range(2000, 2009):
    print('%s 年的生肖是 %s: ' %(year, chinese_zodiac[year % 12]))
"""
import time

num = 5
while True:
    num += 1
    if num == 20:
        break
    print(num)
    time.sleep(1)