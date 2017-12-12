"""
    递归:
        python默认100层递归
        设置递归的层数: sys.setrecursionlimit(x)
        1,有调用函数自身的行为
        2,有一个正确的返回条件

"""

# def recursion():
#     return recursion()
#
# recursion()

# 用递归求阶乘
# 例如:求5的阶乘: 则阶乘式为: 1*2*3*4*5=120

# 非递归版本:

def fun1(x):
    print("%d的阶乘为: " % x, end='')
    temp = 1
    for i in range(1, x+1):
        if(i == x):
            print(i, '=', end='')
        else:
            print(i, '*', end='')
        temp *= i

    print(temp)

fun1(5)

# 递归版本
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))



