"""
    面向对象
        定义对象: 对象 = 属性(静态特征)+方法(动态的动作)
        
    面向对象的特质:
        1,封装--信息隐蔽技术
        2,继承--子类自动共享父类之间的数据和方法机制
        3,多态--不同对象对同一方法响应不同的行动
"""

# 类对象
class Turtle: # 类名是以大写字母开头的

    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print('乌龟会爬')

    def run(self):
        print('乌龟会跑')
    def bite(self):
        print('乌龟会咬人')

    def eat(self):
        print('乌龟会吃东西')

    def sleep(self):
        print('乌龟会睡觉')

# 类的实例化
tt = Turtle()
tt.bite()

list1 = [2, 1, 45, 5, 6, 32]
list1.sort()
print(list1)
list1.append(9)
print(list1)

# 继承
class MyList(list):
    pass

list2 = MyList()
list2.append(1)
list2.append(4)
list2.append(67)
list2.append(10)
print(list2)
list2.sort()
print(list2)


# 多态
class A:
    def fun1(self):
        print('我是小A...')

class B:
    def fun1(self):
        print("我是小B...")

a = A()
b = B()
a.fun1()
b.fun1()


