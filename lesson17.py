"""
    字典2:
    访问字典的方式:
        
"""

# fromkeys(s[,v])
dict1 = {}
dict1.fromkeys((1, 2, 3))
print(dict1.fromkeys((1, 2, 3)))
dict1.fromkeys((1, 2, 3), 'number')
print(dict1.fromkeys((1, 2, 3), 'number'))

dict2 = dict1.fromkeys(range(32), '赞')
print(dict2)


for eachKey in dict2.keys():
    print(eachKey)

for eachValue in dict2.values():
    print(eachValue)


for eachItem in dict2.items():
    print(eachItem)


# print(dict2[32])

print(dict2.get(31))
print(dict2.get(32, 'ok'))


a = {'姓名: ': '大鱼'}
b = a
print(a)
print(b)
# a = {}
# print(a)
# print(b)
a.clear()
print(a)
print(b)

print(dict2.pop(2))


print(dict2.setdefault(50, '好'))
print(dict2)


b = {'小白':'一直傻猫'}
dict2.update(b)
print(dict2)
