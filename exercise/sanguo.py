#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 13:59
# @Author  : Neo
# @Site    : 
# @File    : sanguo.py
# @Software: PyCharm

# 读取人物名称
read_file = open('name.txt', 'r', encoding='utf-8')
data = read_file.read()
data_process = data.split('|')
print(type(data_process))
print(data_process)

# 读取兵器名称
read_file2 = open('weapon.txt', 'r', encoding='utf-8')
i = 1
for line in read_file2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1
print(line)

# 读取三国文本
read_sanguo = open('sanguo.txt', 'r', encoding='GB18030')
print(read_sanguo.read().replace('\n', ''))