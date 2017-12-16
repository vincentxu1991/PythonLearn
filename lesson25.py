"""
    组合-要求定义一个类,里面有乌龟和鱼
        把类的实例化放到一个新类里面,会把旧类组合,不使用继承
        
        
    mix-in编程模式
    
    类,类对象和实例对象
        不要试图在一个类里定义出所有能想到的特性和方法,应该利用继承和组合机制来扩展
        用不同的词性命名,如属性名用名词,方法名用动词
        
    什么是绑定?
        Python要求方法必须有实例才能被调用,这就是绑定,一般来讲,增加参数(self)就是绑定了,
    
        
"""

class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)


    def print_num(self):
        print('乌龟%d只,鱼%d只' % (self.turtle.num, self.fish.num))


pool = Pool(1, 10)
pool.print_num()


class C:
    count = 0


a = C()
b = C()
c = C()

print(a.count)
print(b.count)
print(c.count)

c.count += 10
print(a.count)
print(b.count)
print(c.count)

C.count += 100
print(a.count)
print(b.count)
print(c.count)

