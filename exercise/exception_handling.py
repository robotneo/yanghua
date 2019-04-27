#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 11:46
# @Author  : Neo
# @Site    : 
# @File    : exception_handling.py
# @Software: PyCharm

# i = j   # NameError 变量未定义的错误
# print())    # SyntaxError 语法错误

# a = '123'
# print(a[3])     # IndexError 下标出错

# d = {'a':1, 'b':2}
# print(d['c'])   # KeyError 字典key超出
# year = int(input('input year: '))   # ValueError 输入的非数字

# try:
#     year = year = int(input('input year: '))
# except ValueError:  # 捕获值错误
#     print('年份要输入数字')

# a = 123
# a.append()  # AttributeError: 'int' object has no attribute 'append'

# try:
#     a = 123
#     a.append()
# except AttributeError:
#     print('整数类型没有append()属性')

# try:
#     print(1/"a")
# except (ZeroDivisionError, TypeError) as e:
#     print('0不能做除数 %s' %e)


# try:
#     print(1/"a")
# except Exception as e:
#     print('%s' %e)

try:
    file = open('name.txt')
except Exception as e:
    print(e)
finally:
    file.close()