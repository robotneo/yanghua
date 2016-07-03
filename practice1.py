# 编写一个能够计数的程序。让用户输入起始数字，结束数字以及计数的步数
# 算法设计
# 计数就是显示数字的增减情况

begin = int(input("请输入起始数: "))
end = int(input("\n请输入结束数: "))
interval = int(input("\n请输入步数: "))  # interval 间隔

# 用for循环进行计数显示.
# 分两种情况，如果begin > end 就是向后计数 那么interval必须小于0，如否则就相反
if interval != 0:
    if begin < end:
        # 那么interval 必须是大于0
        # interval = int(input("\n请输入步数: "))
        if interval > 0:
            for interval in range(begin, end, interval):
                print(interval, end=" ")
        else:
            input("请重新输入步数(必须大于0):")
            for interval in range(begin, end, interval):
                print(interval, end=" ")
    elif begin > end:
        # interval = int(input("\n请输入步数: "))
        if interval < 0:
            for interval in range(begin, end, interval):
                print(interval, end=" ")
        else:
           input("请重新输入步数(必须大于0):")
           for interval in range(begin, end, interval):
                print(interval, end=" ")
    else:
        print("你输入的步数不合法.")
else:
    print("你输入的步数不合法.")
