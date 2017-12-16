"""
    self:当对象被调用后,self会作为第一个参数传给方法
    
    __init__(self):构造方法,当实例化一个对象的时候,那么这个方法就会在对象被创建的时候自动调用__init__()方法
        可以重写此方法,进行对象初始化
        
    公有和私有:
        默认:对象的属性和方法都是共有的;通过.操作符访问
        私有:通过name mangling(名字重写,名字改编)技术,只需要在私有的属性和方法前增加__就可以
"""

# class Ball:
#
#     def setName(self, name):
#         self.name = name
#
#     def kick(self):
#         print("my name is %s"%self.name)
#
#
# ball = Ball()
# ball.setName('足球')
# ball.kick()


class Ball:

    def __init__(self, name):
        self.name = name

    def kick(self):
        print("my name is %s"%self.name)


ball = Ball('hello')

ball.kick()


class Person:
    name = 'Vincent'
    __todu = 'todo'

    def get_todo(self):
        return self.__todu

p = Person()
print(p.name)

print(p.get_todo())




