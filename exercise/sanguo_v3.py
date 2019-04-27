#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 15:59
# @Author  : Neo
# @Site    : 
# @File    : sanguo_v3.py
# @Software: PyCharm

import re
def find_main_charecters(charecter_name):
    with open('sanguo.txt', 'r', encoding='GB18030') as f:
        data = f.read().replace("\n", "")
        name_num = re.findall(charecter_name, data)
        # print('主角 %s 出现了 %s 次' %(charecter_name, len(name_num)))
    return charecter_name, len(name_num)
# find_main_charecters("曹操")

# 人物信息
name_dict = {}  # 定义字典存储人物所对应的次数
with open('name.txt', 'r') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            char_name, char_number = find_main_charecters(n)
            name_dict[char_name] = char_number
        # print(name_dict)

# 兵器信息
weapon_dict = {}    # 定义字典存储兵器所对应的次数
with open('weapon.txt', 'r', encoding='utf-8') as f:
    i = 1 # 初始化从第一行开始
    for line in f.readlines():
        if i % 2 == 1:  # 剔除空行 奇数行提取出来
            weapon_name, weapon_number = find_main_charecters(line.strip("\n"))
            weapon_dict[weapon_name] = weapon_number

name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[1:10])

weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
print(weapon_sorted[1:10])