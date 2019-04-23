#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time    : 2019/4/23 8:52
# @Author  : yanghua
# @Site    : hangzhou
# @File    : text_derivative.py
# @Software: Visual Studio Code

#列表推导式和字典推导式

# eg: 求1到11之间偶数的平方

alist = []  #定义列表
print(type(alist))
for i in range(1, 11):
    if(i % 2 == 0):
        alist.append(i*i)
print(alist)

#列表推导式(推荐)
list_derivative = [i*i for i in range(1, 11) if(i % 2 == 0)]
print(list_derivative)

# eg: 求1到100之间的奇数的平方 并打印平方和
list_odd=[] #定义奇数列表
for i in range(1, 100):
    if (i % 2 == 1):
        list_odd.append(i*i)
print(list_odd)
print(sum(list_odd))

#列表推导式(推荐)
list_oddnum = [i*i for i in range(1, 100) if (i % 2 == 1)]
print(list_oddnum)
print(sum(list_oddnum))

#使用列表推导式, 利用方法remove剔除偶数
x = [i*i for i in range(1, 100)]
for i in x:
    if (i % 2 == 0):
        x.remove(i)
print(x)
print(sum(x))

#常规写法
dict_num = {}   #定义字典
print(type(dict_num))   #打印定义的数据类型

for i in dict_num:
    dict_num[i] = 0 #初始化字典key的值都为0

#字典推导式
dict_num = {i:0 for i in dict_num}  #初始化字典key的值都为0
