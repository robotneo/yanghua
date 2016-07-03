local x = 1
local y = 2
print(x)
print(y)
print(type(x))
print(type(y))
ta = {1,2,3,4} -- table数据类型  type()  checkout是什么类型数据
print(type(ta))
tab1 = {key1 = "value1" , key2 = "value2", "value3"}
for k, v in pairs(tab1) do  -- 迭代pairs函数是table专用  ipaies是迭代数组的  迭代字符串的字母string.gmatch
	print(k .. "-" .. v)
end