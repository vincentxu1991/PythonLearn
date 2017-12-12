"""
匿名函数:
    lambda表达式:冒号的前面是函数的参数,冒号的后面是原函数的返回值
    1,python在写一些执行脚本的时候,可以使用lambda函数,可以省下定义函数的过程,
    比如写个简单的脚本管理服务器时间,我们不需要专门定义一个函数再调用,直接使用lambda函数使代码更精简
    2,对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数,起名字很纠结,使用lambda就不需要考虑命名问题了
    3,简化代码的可读性,无需再去找函数def部分- -!
    
filter(函数,可迭代的序列)函数:
    将任何非true的内容过滤掉
    
map(函数,可迭代的序列)函数:映射
    将序列的每个数值作为函数的参数运算加工,直到每个元素加工完毕,返回加工后的新序列
    

    
    
"""
def ds(x):
    return 2*x + 1

temp = ds(5)
print(temp)

g = lambda x: 2 * x + 1
print(g(5))

def add(x, y):
    return x + y

print(add(3, 4))

a = lambda x, y : x + y
print(a(4, 3))


# filter()过滤器
# help(filter)

print(filter(None, [1, 0, False, True]))
print(list(filter(None, [1, 0, False, True])))
# 利用filter筛选出奇数

def is_ji(x):
    return x % 2

temp1 = range(1, 10)
show = filter(is_ji,temp1)
print(list(show))

show1 = filter(lambda x: x % 2, range(1, 10))
print(list(show1))

print(list(map(lambda x: x + 2, range(1, 10))))



