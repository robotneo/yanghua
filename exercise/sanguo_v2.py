#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 14:32
# @Author  : Neo
# @Site    : 
# @File    : sanguo_v2.py
# @Software: PyCharm

# 定义一个函数，读取统一文件
# def read_file(file_name):
#     print(open(file_name, 'r', encoding='utf-8').read())
#     #print(file.read())
#
# read_file('name.txt')

import re
def find_item(hero):
    with open('sanguo.txt', 'r', encoding='GB18030') as f:
        data =f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        # print('主角 %s  出现 %s  次' % (hero, len(name_num)))
    return len(name_num)


# find_item('曹操')

name_dict = {}
# 读取人物信息
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num

name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])

