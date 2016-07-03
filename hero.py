# Hero's Inventory   英雄存货

# 元组的演示

inventory = ()
print(type(inventory))  # 空的元组类型

if not inventory:
    print("You are empty-handed.") # 空指针

input("Press the enter key to continue.") # 按回车键继续

# 创建一个带有一些内容的元组
inventory = ("sword", "armor", "shield", "healing potion")

# 打印元组
print("\nThe tuple inventory is:")
print(inventory)
print(inventory[2]) # 元组也是序列的一种，只是不能修改，固定的，可以用下标获取
# inventory[2] = "yanghua" # TypeError: 'tuple' object does not support item assignment
# print(inventory)

# 打印元组中的各个元素
print("\nYour items:")
for item in inventory:
    print("\n"+item)

input("\nPress the enter key to continue.")

# 获取元组的长度
print("You have", len(inventory), "items in your possession.")

input("\nPress the enter key to continue.")

# 测试healing potion是不是inventory里面的成员

if "healing potion" in inventory:
    print("\nTrue")

# 对元组的索引方式
index = int(input("\nPress the index number for an item in inventory:"))
print("At index", index, "is", inventory[index])

print("\nPress the enter key to continue.")

# 对元组的切片

start = int(input("\nPress the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[",start, ":", finish, "] is ", end=" ")
print(inventory[start:finish])
input("\nPress the enter key to continue.")

# 元组不可变性（immutable）

# 元组的连接操作，设定2个元组 +=连接，只需要直接用连接运算符+连接

chest = ("gold", "gems")
print("You find a chest. It contains: ", end = " ")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
