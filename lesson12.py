"""
    global关键字:强制变为全局变量
    nonlocal关键字: 强制声明不是一个局部变量
    
    内嵌函数(内部函数):允许在函数内部创建另外一个函数
        内部函数的使用:内部函数的整个作用域,都在外部函数之内->导致了,只有通过外部函数才能调用该内部函数
        
    闭包:
        如果在一个内部函数里,对外部作用域引用的变量,那么就说这个内部函数为一个闭包
"""
count = 5
def myFun():
    count = 10
    print(count)
myFun()
print(count)

def myFun():
    global count
    count = 10
    print(count)
myFun()
print(count)

def fun1():
    print("fun1()正在被调用")
    def fun2():
        print("fun2()正在被调用")
    fun2()
fun1()

#fun2()

#闭包
def funX(x):
    def funY(y):
        return x * y
    return funY

i = funX(8)
print(i)
print(type(i))
j = i(5)
print(j)
temp = funX(10)(5)
print(temp)

# def fun3():
#     x = 5
#     def fun4():
#         x *=x
#         return x
#     return fun4


def fun3():
    x = [5]
    def fun4():
        x[0] *=x[0]
        return x[0]
    return fun4()
print(fun3())

def fun5():
    x = [5]
    def fun6():
        x[0] *=x[0]
        return x[0]
    return fun6()
print(fun3())
