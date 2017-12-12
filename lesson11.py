"""
 Python只有函数,没有过程
 如果在函数内试图修改全局变量的值,那么Python会创建一个新的局部变量代替这个全局变量
"""

def hello():
    print("hello world")

temp = hello()

def back():
    return [1, 2, 3, 4, [5, 6, 7, 8]]

temp1 = back()
print(temp1)

print(back())

""""""


