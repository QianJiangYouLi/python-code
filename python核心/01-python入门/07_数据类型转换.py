# 类型转换就是将一个类型的对象转换为其他对象
# 类型转换不是改变对象本身的类型，而是将对象的值转为新的对象。
# 类型转换四个函数：int、float、str、bool，它们都不会修改原来的变量，而是将对象转为指定类型并返回，要改变原来的变量，需要重新赋值
# int转换规则：布尔值True转为1，False转为0。浮点数直接取整，没有进位。合法整数数值字符串会转为整数，其它的会报错。
# float转换规则与int基本一致，只是转为浮点数
# str可以将对象转为字符串
# bool可以将对象转为布尔值，任何对象都可以转为布尔值，对所有表示空性的对象都会转为False，其他的都是True
a = True
a = int(a)
print(a)

a = 'hello'
b = 123
# print(a+b) TypeError: can only concatenate str (not "int") to str
print(a+str(b))

a = 1
print(bool(a))
b = 0
print(bool(b))
c = ''
print(bool(c))
d = 'str'
print(bool(d))
