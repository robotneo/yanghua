# print("yanghua")
# y = 12
# print(y)
# number = 87
# print(type(number))   --和lua的语法差不多--
# print(number)
# Game Over - Version 2
print("Program 'Game Over' 2.0")
print("Same", "message", "as before")
print("Just", "a big", "bigger")
print("Here", end="--")
print("it is...")

input("\n\nPress the enter key to exit.")
# yanghua
# 演示转义序列
print("\t\t\tYangHua")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")
print("\t\t\tby")
print("\t\t\tYangHua")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")

print("\n特别鸣谢以下人员:")
print("My hair stylist,Henry\'The Great,\' who never says \"can\'t.\"")
#响一下电脑蜂鸣器
print("\a")
input("请按任意键退出....")

print("何必如此，我们都是一起长大的，就应该互助互爱" \
      +"jkdgskdjhoqhwoiuehiwq")
print("pie"*10)
#整除法  双 //  小数部分会直接忽略，直接显示整数部分 其他的算数运算符都和java一样
print(20//3)
name = "yanghua"
print(type(name))
print(name)
names = input("请输入你的名字:")
print(names)
print("欢迎使用本程序，很高心为你服务" + names)
quote = "I think there is a world market for maybe five computers."
print(quote)
print("\nIn uppercase:")#小写转大写
print(quote.upper())
print("\nIn lowercase:")#大学转小写
print(quote.lower())
print("\nAs a title:")#标题的形式展示出来
print(quote.title())
print("\nWith a ,minor replacement") # 替换字符串信息
print(quote.replace("five","millions of"))
print("\nOriginal quote is still:")
print(quote)
input("请按任意键退出。")
# 大小写互换是swapcase()
word = "I Love you , You Are LIKE food"
print(word.swapcase())
input("按任意键退出程序。")
print("接下来是一个大小写转换的程序。")
# 程序开始
field = input("请输入你要转换的字母或英文字段: ")
print("1-大写转小写，2-小写转大小写，3-互转，4-标题形式")
number = int(input("请输入你要进行的操作:"))
print(number)
if number == 1:
    print(field.lower())
elif number == 2:
    print(field.upper())
elif number == 3:
    print(field.swapcase())
elif number == 4:
    print(field.title())
else:
    print("你输入的不是字母或英文字段")
input("请按任意键退出.")
# 字符串转换问题
# upper()  字符串大写
#和Java一样，有符合运算符，如:*= += -= /= %=
span = 4
span *= 5
print(span)