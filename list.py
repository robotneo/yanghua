# Hangman

# 列表 相当于Java中的数组 []
inventory = ["sword", "armor", "shield", "healing potion", "helmet", "gold"]
print("Your items:\n")
for item in inventory:
    print(item, end=" ")

input("\n\nPress the enter key to continue.")

# 获取列表的长度
print("\nYou have", len(inventory), "items in your possession.")

input("\nPress the enter key to continue.")

# 利用in测试成员关系

if "healing potion" in inventory:
    print("You will live to fight anther day.")

# 对列表进行索引
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", "'"+inventory[index] +"'")

# 对列表进行切片，Java中subString()

start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("\nEnter the index number to end a slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

# 两个列表连接
chest = ["gems", "necklace"]
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("You inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

# 列变和元组，元组是圆括号，列表是方括号，列表可变，元组固定
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now:")
print(inventory)

input("\nPress thee enter key to cintinue.")

# 检查列表元素是不是唯一性
a = ["a", "v", "v", "h", "q"]
print(a)
print(len(a))
# 不是唯一性

# 通过切片对列表元素赋值
print("You use your helmet and gold to buy an orb of futurn telling.")
inventory[4:6] = ["orb of futurn telling"]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")
# 删除列变元素
print("In a great battle, your shield is destoryed.")
del inventory[2] # 删除del
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

# 删除列表切片
print("删除列表切片，如从下表0开始，到下表2的位置。")
del inventory[:2]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")


