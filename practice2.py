# 编写一个程序，获取用户输入的一天信息，然后将其倒序输出
# 算法设计
# 首先获取用户输入的信息，然后获取后续index

message = input("请输入一段信息:")
print("你输入的信息是:%s "%(message))

for i in range(-1, -len(message)-1, -1):
    print(message[i],end=" ")
