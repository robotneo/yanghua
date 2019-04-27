#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 10:42
# @Author  : Neo
# @Site    : 
# @File    : file_open.py
# @Software: PyCharm

"""
# 将小说的人物添加到文件中
file1 = open('name.txt', 'w')
file1.write('1 诸葛亮' + '\n')
file1.write('2 独孤求败' + '\n')
file1.close()

# 从文件中读取人物信息
file2 = open('name.txt', 'r')
print(file2.read())
file2.close()

# 从文件中追加内容 不覆盖 往后添加
file3 = open('name.txt', 'a')
file3.write('3 杨过' + '\n')
file3.write('4 风清扬' + '\n')
file3.close()

# 读取单行
file4 = open('name.txt', 'r')
print(file3.name)   #读取的文件的名字
print(file4.readline())     #循环读取第一行开始
print(file4.readline())
print(file4.readline())

# 循环读取
file5 = open('name.txt', 'r')
for line in  file5.readlines():
    print(line)
    print('=============')

file5.close()
# 推导式
file6 = open('name.txt', 'r')
line_str = [line for line in file6.readlines()]
print(line_str)
file6.close()

"""
# 操作指针
file_read = open('name.txt', 'r')
print('当前文件指针的位置: %d' %file_read.tell())
print('当前读取到一个字符，字符的内容是: %s' %file_read.read(1))
print('当前文件指针的位置: %d' %file_read.tell())


# 第一个参数代表偏移的位置，第二个参数代表 0表示从文件开头偏移，1表示从当前位置偏移，2表示从文件结尾
file_read.seek(5, 0)

print('我们进行了seek，指针的重置')
print('当前文件指针的位置: %d' %file_read.tell())
print('当前读取到一个字符，字符的内容是: %s' %file_read.read(1))
print('当前文件指针的位置: %d' %file_read.tell())

file_read.close()