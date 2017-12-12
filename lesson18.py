"""
    集合:
        元素具有唯一性,且无序
"""

num = {}
print(type(num))

num2 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
print(type(num2))
print(num2)


num3 = set([1, 2, 3, 4, 5, 6, 5, 3, 2])
print(num3)

num1 = [1, 2, 3, 4, 5, 5, 3, 1, 0]
set1 = set(num1)
print(set1)

num1 = list(set(num1))
print(num1)

num3 = frozenset([1, 2, 3, 4, 5])
set1.add(10)
print(set1)


