# if 后面跟上别的类型数据也可以当做条件
# 值转换为True 和 False 很简单，基本原则就是: 任何空值或零值都为False。其他的True

# 打印0--10之间的数字，跳出5这个数字

count = 0
while True:
    count += 1
    # 如果count > 10 就退出循环
    if count > 10:
        break
    # 如果等于5就跳出过5
    if count == 5:
        continue
    print(count)
input("请按回车键退出程序")
# 简单条件  simple condition

# 复合条件  compound condition
print("\t\t欢迎来到精英网络会所")
print("\tExclusive Computer Network")
print("\t\tMembers only！\n")

security = 0
username = ""  # 为空值
print(type(username))
# 任何空值或零值都为False。
while not username:
    username = input("Username: ")
password = ""

while not password:
    password = input("Password: ")

if username == "M.Dawson" and password == "123456":
    print("Hi, Mike")
    security = 5
    print("你的账户安全等级为: %d"%security)
elif username == "S.Meire" and password == "123456":
    print("Hi, Jack")
    security = 3
    print("你的账户安全等级为: %d"%security)
elif username == "W.Wright" and password == "456789":
    print("Hi,Smith")
    security = 4
    print("你的账户安全等级为: %d"%security)
elif username == "Guest" or password == "Guest":
    print("Welcome,guest")
    security = 1
    print("你的账户安全等级为: %d"%security)
else:
    print("Login failed. You're not so exclusive.\n")
input("请输入回车键退出")


# Gusee My number
# 计算机随机挑取0--100之间的数字

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in ad few attempts ad possible.\n")

the_number = random.randint(1,100)

guess = int(input("Take a guess: "))

tries = 1

# 猜测循环
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    
    tries += 1
    
    print("You guess it! The number was :",the_number)
    print("And it only took you",tries,"tries!\n")
input("\n\nPress the enter key to exit.")


