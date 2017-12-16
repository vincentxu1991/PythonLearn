"""
    继承:
        class DerivedClassName(BaseClassName):
            .....
    
    子类可以继承父类的任何属性和方法
    如果子类中定义与父类同名的方法或属性,则会自动覆盖父类对应的方法与属性
    
    多重继承:
        class DerivedClassName(Base1,Base2,Base3):
            ....
"""

# class Parent:
#
#     def hello(self):
#         print('正在调用父类的hello方法')
#
#
# class Child(Parent):
#
#     pass
#
# p = Parent()
# p.hello()
#
# c = Child()
# c.hello()

class Parent:

    def hello(self):
        print('正在调用父类的hello方法')


class Child(Parent):

    def hello(self):
        print('正在调用子类的hello方法')


p = Parent()
p.hello()

c = Child()
c.hello()
import random as r

class Fish:

    def __init__(self):
        self.x = r.randint(1, 10)
        self.y = r.randint(1, 10)

    def move(self):

        self.x -= 1
        print('my points is :', self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):

    def __init__(self):

       # Fish.__init__(self) # 调用未绑定的父类方法,参数给的是子类的self对象
        # 使用super函数
        super().__init__()
        self.hungry = True

    def eat(self):
        if(self.hungry):
            print("我饿了,我要吃")
            self.hungry = False
        else:
            print("吃饱了")

fish = Fish()
fish.move()

fish.move()
goldFish = Goldfish()
goldFish.move()
shark = Shark()
shark.eat()
shark.eat()
shark.move()





class Base1:

    def foo1(self):
        print('我是Base1中的Foo1')

class Base2:

    def foo2(self):
        print('我是Base2中的Foo2')

class Base3:
    def foo3(self):
        print('我是Base3中的Foo3')


class C(Base1,Base2,Base3):
    pass

c = C()
c.foo2()
c.foo1()
c.foo3()



