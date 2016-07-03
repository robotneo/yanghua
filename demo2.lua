print("hello lua")
--第一个lua程序 单行注释--
print("hello world")
--局部变量
local number = 67
print(number)
--[[我今天过来主要是为了学习lua 多行注释--]]
local name = "yanghua"
print(name)
print(type(name))
--定义变量的关键字[local]
print(1);print(2) --多个语句在同一行可以用分号隔开--
--控制语句
if 1+1==2 then print("true")
	elseif 2+3==5 then print("true")
	else print("false")
	end
--循环语句
while 1+4==3 do print("true") end

for x = 10,1,-1 do
	print(x)
end

y = 100 -- 没加local就是全局变量
repeat
	print("y的值为:",y)
	y = y + 10
until(y > 150) -- 必定会种执行一次，相当于Java中的do --while()
local i = 23
print(type(i))
print(type(true))
print(type(print)) --封装好的函数，打印函数 函数类型function

ta = {1,2,3,4} -- table数据类型  type()  checkout是什么类型数据
print(type(ta))
tab1 = {key1 = "value1" , key2 = "value2", "value3"}
for k, v in pairs(tab1) do  -- 迭代pairs函数是table专用  ipaies是迭代数组的  迭代字符串的字母string.gmatch
	print(k .. "-" .. v)
end

-- 字符串专用 string.gmatch
local word = "abcdefg"
for w in string.gmatch(word, "%l") do  --正则表达式 %l换行
	print(w)
end
tab2 = {key1 = nil , key2 = "value2", nil}
for k, v in pairs(tab2) do
	print(k .. "-" .. v)
end

--定义变量为nil，其实也是把该变量删除
--定义一个时间event,该事件判断具体执行的任务是什么
local maxset = 2^4  --局部变量  支持幂运算
print(maxset)

--选择一个计数器，记录每一个数的值
function add(a,b)
	--返回数值
	return a*b
end
print(add(3,7))

--写一个简单的计算器
--共有5种运算，+，-，*，/,^
function calculator_counter(a,b,c)
	-- 利用判断语句来选择执行什么运算
	if b=="+" then
	   print(a+c)
	elseif b=="-" then
	    print(a-c)
	elseif b=="*" then
	    print(a*c)
	elseif b=="" then
		print(a/c)
	elseif b=="^" then
		print(a^c)
	else
		print(false)
	end
end

print(calculator_counter(4,"*",2))
print(calculator_counter(5,"-",2))
print(calculator_counter(9,"^",3))
num = function(b)  --第二种函数的表达方式
	b = b + 5
	print(b)
	end
num(2)
print(num(1))

function cangLaoShi( i )
	print(i)
end
do
	local jiese = "苍老师的教学片我很喜欢"  --哈哈，逗你们玩了
	cangLaoShi(jiese)
end

--输出1~100之间能被7整除的数
--for循环做出来的
--[[ for i=1,100 do
	if i%7==0 then
	    print(i)
	end
	i = i + 1
end--]] 
--while循环做出来的
local x = 1
while x < 100 do
	if x%7==0 then
	    print(x)
	end
	x = x + 1
end
--定义一个函数，利用循环让这个函数能计算n的阶乘
--如: 5*4*3*2*1
--定义两个变量i,j
--[[ for i=1,10 do
	--local j = 1
	sum = 1
	sum = sum * i
	--j = j + 1
	i = i + 1
	print(sum)
end--]] 
test = function(n)
local q = 1	
if n < 1 then
    n = 1
end
repeat
	q = n * q
	n = n - 1
until n == 0
	print(q)
end
print(test(10))

for i=1,10,1 do
	if i == 8 then
	    break
	end
	print("这是第"..i.."次循环")
end

for i=1,100,20 do
	if i > 70 then
	    break
	end
	print(i)
	os.execute()
end
-- io.output():write
-- io.output():read
-- io.input():read
-- io.input():write
--定义一个函数来检测io.read()
function fact( n )
	if n==0 then
		return 1
	else
		return n * fact(n-1)
	end
end
print("请输入一个数字")
num = io.read("*number") --读一个数字
print(fact(num))