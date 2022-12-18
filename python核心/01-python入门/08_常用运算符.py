# 算术运算符：加+ 减- 乘*  除/  整除//  取模% 幂运算**
# 加法运算中，两个操作数是字符串会进行拼接
# 字符串与整数相乘会复制字符串
# 除法总会返回浮点数，要取得整数，需要用整除(直接舍去小数)
print(1+2)  # 3
print('ha'+'ha')  # haha
print('ha'*3)  # hahaha
print(10/3)  # 3.3333333333333335
print(10//3)  # 3
print(10 % 3)  # 1
print(2**10)  # 1024

print('-------我是分割线-------')

# 赋值运算符，将右侧的值赋给左侧: = += -+ *= /= //= %= **=
# 注意：与浮点数进行运算，结果是浮点数
a = 5
a += 5  # 等价于 a = a + 5 ，其它一样
print(a)

print('-------我是分割线-------')

# 关系运算符，返回布尔值，成立返回True，否则返回False
#  > < == >=  <=  !=
print(3 > 5)  # False
print(3 < 5)  # True
print(3 >= 5)  # False
print(3 <= 5)  # True
# 相等与不等比较的是值，而不是id。比较两个对象是否相等用的是 is 和 is not，比较是id
print(3 == 5)  # False
print(1 == True)  # True
print(3 != 5)  # True
# 不支持两个不同类型的值进行比较。
# 可以对两个字符串进行比较（比较的是Unicode码，逐位比较）。对中文的意义不大
# 若不希望比较Unicode码，可以进行数据类型转换
print('abc' > 'aHe')  # True

print('-------我是分割线-------')

# 逻辑运算符： not逻辑非，and逻辑与，or逻辑或。主要用于逻辑判断
# not 一元运算符，可以对符号右侧的值进行非运算。取反
# 对于布尔值，直接取反，对非布尔值，会隐式数据类型转换后再取反
print(not True)  # False

# and 只有两侧全是True才是True，其它的都是False
# python中的与运算是短路运算（找False），第一个值为False，其他的都不看了
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(True and False)  # False

# or 只有两侧全是False才是False，其他的都是True
# 或运算找True，也是短路运算，第一个值是True，其它的不看了
print(False or False)  # False
print(True or False)  # True
print(False or True)  # True

# 对非布尔值进行与、或运算会将其当做布尔值运算，结果返回原值
# 如果第一个值是False，则直接返回第一个值，否则返回第二个值
# True and True
print(1 and 2)  # 2
# True and False
print(1 and 0)  # 0
# False and True
print(0 and 1)  # 0
# False and False
print(0 and 0)  # 0

# 或运算找True，如果第一个值是Ture，则不看第二个。如果第一个值是True，返回第一个，否则返回第二个值
# True or True
print(1 or 2)  # 1
# True or False
print(1 or 0)  # 1
# False or True
print(0 or 1)  # 1
# False or False
print(0 or 0)  # 0

print('-------我是分割线-------')

# 三元运算符，有三个操作数
# 语法： 语句1 if 条件表达式 else 语句2
# 执行流程：先对条件表达式进行求值判断，结果为true，执行语句1，结果为false，执行语句2，并返回执行结果
a = 10
b = 20
print(a if a > b else b)  # 20
