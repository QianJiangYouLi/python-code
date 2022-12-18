#  python 变量不需要声明直接使用，但不能使用没有赋值的变量
a = 10
print(a)
a = 'hello'
print(a)

# 标识符不能是关键字或保留字，可以含有字母数字下划线，但不能以数字开头。
# 不要用函数名作为标识符，防止覆盖
# 两种命名方式：驼峰命名或者下划线命名
hello_world = 'hello'
helloWorld = 'Hello'
print(hello_world)
print(helloWorld)
