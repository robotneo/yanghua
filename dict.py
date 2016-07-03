# 字典形式的变量，如其他语言中的Map一样，Key - value 对形式存在 内置的方法，字典
di = {'yanghua': 12, 'yangfan': 23, 'yangyang': 34, 'yangzhi': 56};
print("di['yanghua']:", di['yanghua']);

# 字典就是用相当于map，键值对的形式，声明一个字典{}便是
# list 列表，用[]来声明一个list列表，下标取值

classmates = ['yanghua', 'yangfan', 'yangyang', 'yangzhi']

print(classmates)
print(classmates[2])  # 用下标来取值
print(len(classmates)) # len()用来获取列表的长度
print(classmates[len(classmates)-1])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('yangjiao') # 追加元素，玩列表里面追加元素
print(classmates)

# 在指定位置插入数据
classmates.insert(2, 'JAVK')
print(classmates)
# 删除指定位置的元素，用pop(i)方法   要删除list末尾的元素，用pop()方法
# list里面的元素可以是list，如:
s = ['python', 'java', ['asp', 'php'], 'scheme', 'C++', 'Ruby', 'Lua', 'Javascript']

print(s)

print(s[2])
print(s[2][1]) # 二维就是数组的形式
# list可以存储不同的数据类型 如：
list1 = ['yanghua',23,True,False,2.18];
print(type(list1))
print(list1[2])

# list类型的声明是以[]来声明，创建
# 字典 也就是和其他语言相同的Map 是以{} 来创建

# 元组 有序列表的一种， tuple元组，一旦声明变量，不可以改变里面的东西
# 元组的定义，有情况  以()来定义元组的，就是不可以改变长度，删除
t = ('a', 'b', ['A', 'B'])
print(type(t))
print(t[1])
print(t[2][0])
print(t[2][1])

# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# s要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(type(s))
print(s)

# 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

# 重复元素在set中自动被过滤：
se = set([1, 2 ,3 ,3, 3, 3])
print(type(se))
print(se)

# set语法  set([元素1，元素2，元素3])，不能重复值，无序的列表形式
se.add(4)
print(se)
se.remove(4)
print(se)
# set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

# 再议不可变对象
 
# 上面我们讲了，str是不变对象，而list是可变对象。
# 对于不可变的对象或者比变量怎么保存

see = "abcd"  #改变字符创的总府大小写
b = see.replace('a', 'A')
print(b)

# -*- coding: utf-8 -*-

temp = int(input("Please enter a number:"))
he = hex
print('The hex is:'+he(temp))

yang = print
yang("yanghua")
# python 中内置的函数，可以弄一个变量保存该内置的函数名，那么就是别名，可以代替该函数
# 就如打印这个函数print可以赋值给一个变量，那么这个变量就可以当做打印的功能使用
yang = print
yang("yanghua")
# abs() 球绝对值的函数 max() min()  help(abs)
help(abs)  # 返回abs的函数使用信息

# 数据类型转换就不会说了，很简单

# 定义函数 def
# def 函数名(参数1,，，参数n): 代码块

def fun(a,b):
    if a > b:
        print(b)
    else:
        print(a)    
fun(6,9)

# 空函数  如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
# 作用 实际上pass可以用来作为占位符
'''
参数检查

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：

>>> my_abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: my_abs() takes 1 positional argument but 2 were given

'''
# 数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 坐标移动
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

m = move(100, 100, 60, math.pi / 6)
print(type(m))
print(m)


    
