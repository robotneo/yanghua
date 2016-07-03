# for 循环是根据序列sequence

# 序列中么偶一个元素element
word = input("enter a word: ")
print("\nHere's each letter in your word:")
for letter in word:
    print(letter)
input("\n\nPress the enter key to exit")


# range()该函数用在for循环中

# 计数器， Counter
print("Counting:")
for i in range(10):  # 递增
    print(i, end=" ") # 前闭后开
print("\n\nCounting by fives:")  # 以五作为一个循环计数
for i in range(0, 50, 5):
    print(i, end=" ")
print("\n\nCounting backwards:")
for i in range(10, 0, -1):  # 递减
    print(i, end=" ")

input("\n\n\n输入回车键退出。")

# range()是以起始点，结束点，计数单位。为参数，包含起始点，不包含结束点

# Random Access(使用，存取)
# 演示字符串的索引

import random

word = "index"
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[",position, "]\t", word[position])
input("\n\nPress the enter key to exit.")

# 序列分为两种的，可变，和不可变的

# 演示利用for循环来创建新的字符串

message = input("Enter a message: ")
new_message = ""
VOLWELS = "aeiou"  # 元音字母


print()
for letter in message:
    if letter.lower() not in VOLWELS:
        new_message += letter
        print("A new string has been created: ", new_message)
print("\n\nYour message without vowels is:", new_message)
input("\n\nPress the enter key to exit.")


# 切片  slice

word = "pizza"

print(
    """
    Slicing 'Cheat Sheet'

    0   1   2   3   4   5
    +---+---+---+---+---+
    | p | i | z | z | a |
    +---+---+---+---+---+
   -5  -4  -3  -2  -1
   
    """
    )

print("Enter the begining and ending index for your slice pf 'pizza'.")
print("Press the key enter key at 'Begin' to exit")

start = None
while start != "":  # 只要start不为空就一直执行下去的程序
    start = input("\nStart: ")

    if start:
        start = int(start)

        finish = int(input("Finish: "))

        print("word[", start, ":", finish, "] is", end=" ")
        print(word[start:finish])
input("\n\nPress the enter key to exit.")


