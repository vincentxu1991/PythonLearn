"""
    类的内置函数:
        issubclass(class, classinfo) 判断一个类是否是其自身的子类;
            classinfo 是一个元组,class与其任何一个候选类的子类,则返回true
        isinstance(obj, classinfo) 判断一个实例对象是否属于一个类
            obj:实例参数对象,必须为对象,要不然会永远返回false
            classinfo:需要被检查的类(元组),必须由类组成,不然会抛出一个TypeError异常
            
        hasattr(obj,name):测试一个对象是否有指定的属性,name必须用字符串串起来,不然会抛出NameError的异常
        getattr(obj, name[, default]):返回对象指定的属性值,如果对象不存在,会打印default,
            若default未设置,则抛出AttributeError一个异常
            
        setattr(obj,name,value)设置指定属性的值,若属性不存在,则新建该属性并赋值
        delattr(obj,name)删除对象中指定的属性,若属性不存在,则抛出AttributeError的异常
        
        property(fget= none, fset =null,fdel = none,doc = none)通过属性来设置属性
            获取属性的方法,设置属性的方法,删除属性的方法,
        
            

"""

class A:
    pass

class B(A):
    pass

print(issubclass(B, A))
print(issubclass(B, B))
print(issubclass(A, B))
print(issubclass(A, object))


class C:
    def __init__(self, x=0):
        self.x = x

c1 = C()
print(hasattr(c1, 'x'))

print(getattr(c1, 'x'))
print(getattr(c1, 'y', 10))


class D:
    def __init__(self, size =10):
        self.size = size

    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)

d = D()
print(d.x)
d.x = 20
print(d.x)
del d.x
print(d.x)


