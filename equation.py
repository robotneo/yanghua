# -*- coding: utf-8 -*-
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

# ax2 + bx + c = 0

# 的两个解。
import math

print("该程序是计算一元二次方程的根，欢迎你使用愉快，亲爱的小伙伴！\n")
def quadratic(a, b, c):
# 先判断 a b c三个参数，必须是数字
    for check in (a, b, c):
        if not isinstance(check,(int, float)):
            raise TypeError("错误的数据类型")
    temp = b * b - 4 * a * c  # 由这个条件判断有几个解
    some = (-b)/(2 * a)
    if temp == 0:
        return some
    elif temp > 0:
        x1 = (-b + math.sqrt(temp))/(2 * a)
        x2 = (-b - math.sqrt(temp))/(2 * a)
        return x1,x2
    else:
        return("No Solution")
# 我来一个循环，可以计算任意的一元二次方程
# operate = int(input("请输入要执行的操作: 1-计算，2-退出： "))

while (True):
    operate = int(input("请输入要执行的操作: 1-计算，2-退出： "))
    if operate==1:
        a,b,c=input("请输入一元二次方程的a,b,c三个参数，以‘，’分开：").strip().split(',')
        # 如果输入的数没满足三个参数，如你只输入了一个或者两个参数，会报错，没解决
        # for san in (a,b,c):
        #    if not isinstance(san, (None)):
        # 用‘,’分割数据，并将字符串转换成float数据类型
        # 不知道有没有办法，一行命令转换abc为float数据类型
        a = float(a)
        b = float(b)
        c = float(c)
        print("方程的解(x1,x2):",end="")
        print(quadratic(a, b, c))
    #else:
    #    print("你输入的参数不够，请重新输入")
    #    quadratic(a, b, c)
    elif operate==2:
        input("请回车键退出")
        break
    else:
        input("请回车键退出")
        break
