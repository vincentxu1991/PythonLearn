"""
    函数:
        
"""

def my_first_function():
    print("123")


my_first_function()


def my_second_function(name):
    print(name + "哦")

my_second_function("啦啦啦啦啦")


def add_tow_numbers(num1, num2):
    return num1 + num2

print(add_tow_numbers(10, 11))

#关键字参数
def say_hello(name, words):
    print(name + words)

say_hello(name="我", words="上海")

#默认参数
def say_hello2(name='Vincent', words='money'):
    print(name + words)

say_hello2()
say_hello2('我', '你')


def test1(*params):
    print("参数的长度为: ",len(params))
    print("第二个参数为: ", params[1])

test1(1, '我', '上海', 2, 3, 4)
