# Word Jumble
#
# 计算机随机挑选一个单词，然后把它‘打乱’
# 玩家必须猜出本来的那个单词

import random

# 创建一组可选择的单词常量元组

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS) # random.choice() 随机选取

# 把随机出来的单词赋值给correct变量
correct = word

# 设计算法
# 创建一个空的题目，当 给定的单词中有字母时，从其中随机抽取一个字母，见这个字母添加带题目中

# 创建一个空字符串，保存乱序的单词

jumble = ""

# 乱序的单词怎么形成呢？
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position]+word[(position+1):]  # 获取一个单词，就减去一个单词
# 开始游戏

print(
    """
    \t\tWelcome to Word Jumnle!

    \nUnscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
    )
print("The jumnle is:\t%s"%(jumble))

# 获取玩家的输入答案  guess  猜测
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry,that's not it.")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it! You guess it!\n")
# 结束游戏
print("Thanks for playing.")
print("\n\nPress the enter key to exit.")
