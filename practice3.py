# 创建一个游戏：计算机随机选取一个单词，然后由玩家来猜，
# 计算机先告诉玩家这个单词有多少个字母。
# 玩家只有五次机会，咨询这个字母是否存在某个字母。然后就必须猜出这个单词。

# 导入随机数包
import random
# 创建一组可供选择的单词
WORDS = ("python", "java", "ruby", "perl", "go", "lua", "easy", "answer", "good")

word = random.choice(WORDS)

# 获取word的长度，也就是单词有几个字母组成

print(
    """
    \t\t你好，欢迎来到猜字游戏！
    游戏规则: 该游戏，会随机在单词库中获取单词，并展示该单词的长度，你可以
    询问五次，问我该单词中有哪些字母，一共只有五次机会，你只能问5次，我只会说该字母
    在该单词中是有还是没有，不会说出别的信息，祝你游戏愉快。

    \t\t\t\t--游戏有沉迷性，请勿强求！随缘就好
    """
    )
input("Press the enter key to continue.")

input("你准备好了吗？请按回车键继续！")

print("该单词有 %d 个字母。"%(len(word)))

# 猜测单词
hint = int(input("是否需要询问: 1-是，2-否 "))

if hint == 1:
    # 需要询问
    count = 1
    while count < 5:
        letter = input("请输入你猜测的字母: ")
        if letter in word:
            print("是")
        else:
            print("否")   
        hint = int(input("是否继续询问: 1-是，2-否 "))
        if hint == 2:
            break
            
        count += 1
        if count > 5:
            guess = input("你询问的次数已到了5次，机会已用完。请输入你猜测的单词:")
            break

guess = input("请输入你猜测的单词: ")
if guess == word:
    print("恭喜你，猜对了！")
else:
    print("猜测不对!")

input("Press the enter key to exit.")
