# 创建能以随机数顺序显示一组单词的程序，不能重复

import random

# 创建一个带有一些元素的列表出来

words = ['python', 'java', 'lua', 'html', 'css', 'xml', 'ruby']
print()
print(words)
# 遍历显示出来
print()
print("遍历显示出来：\n")

# print(len(words))

for item in words:
    print(item, end=" ")
    
input("\n\nPress the enter to continue.")
print()
print(len(words))
print()
# 创建乱序版的序列
jumble = []

while words:

    # 随机数显示出来
    position = random.randrange(len(words))

    # print(position)
    # 算法设计，循环遍历WORDS，只要随机下标，就把随机到的单词切片到新的序列中
    jumble.append(words[position])

    # 删除原字符串的随机出来的位置单词
    words = words[:position] + words[(position+1):]

    # 开始
print("乱序版单词，排列在序列中:\n")
print(jumble)

input("\n\nPress the enter key to exit.")
