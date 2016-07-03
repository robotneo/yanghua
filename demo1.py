# 导包 随机数的包
import random

# 生成1到6的随机整数
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("你的第一个筛子的值" , die1, "和你的第二个筛子的值" , die2,"总数" , total)

input("按任意键退出")

print("根据随机数，打印一些表情")

mood = random.randint(1, 3)
print(type(mood))
print("随机数产生的数: %d"%(mood))
if mood == 1:
    #高兴
    print("高兴")
elif mood == 2:
    #一般
    print("一般")
elif mood == 3:
    #难过
    print("难过")
else:
    print("Illegal mood value! (You must be in a really bad mood).")
    print("...today.")
    
    input("\n\n请按回车键退出")


# python格式化字符串 -%s
print("我总是喜欢行走在路得边缘 -%s"%("杨华"))
# python格式化整数
print("在我的家乡肉卖 %d元一斤"%(14))
# python格式化浮点数
print("His height is %fm"%(2.14))# 后面保留6个小数点
# python格式化(指定小数点位数)
print("His height is %.2fm"%(2.14))
# python格式化指定占位符的宽度
print("Name:%10s Age:%8d Height:%8.2f"%("JACK",20,2.15))
# python格式化左对齐
print("Name:%-10s Age:%-8d Height:%-8.2f"%("JACK",20,2.15))
# python格式化指定占位符(0)
print("Name:%-10s Age:%08d Height:%08.2f"%("JACK",20,2.15))
# python格式化(科学计数法)
print(format(0.0015,'.2e'))
