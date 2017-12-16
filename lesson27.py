"""
    魔法方法
        魔法方法被双下划线包围--例如 __init__
        魔法方法是面向对象Python的一切,
        魔法方法体现在他们总能够在适当的时候被自动调用
        
        
        __init__(self[,...])-构造方法,对象初始化的时候调用,init函数不能返回
        __new__(cls[,...])-对象初始化时,调用的第一个方法,第一个参数是class,如果有参数,则参数会传给init方法,返回个初始化的对象
            当继承一个不可变类型的时候且需要修改
            
        __del__(self) 析构器:当对象需要被销毁的时候,会自动调用__del__方法(辣鸡回收机制)
            所有对对象的引用都被del之后,才会自动启动__del__方法.
"""

class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def getPeri(self):
        return (self.x +self.y)*2
    def getArea(self):
        return (self.x * self.y)


rect = Rectangle(3, 4)

print(rect.getPeri())
print(rect.getArea())


class CapStr(str):

    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

a = CapStr('hello')
print(a)

class C:
    def __init__(self):
        print('init方法...')

    def __del__(self):
        print('del方法被调用...')

c1 = C()



