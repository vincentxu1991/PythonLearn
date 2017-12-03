"""
列表类型的小伙伴:

count:计算参数在列表中出现的次数
index(值,开始位置,结束位置):返回参数在列表中的位置

reverse:将列表反转
sort(func,key,reverse=false): 默认从小到大排序额

Copy列表: list1 = list2[:]

"""
list1 = [123]
list2 = [456]
print(list1 >list2)

list3 = [123,456]
list4 = [456,123]

print('shanghai' not in list3)
# print(dir(list))
list3 *=5
print(list3.count(123))
print(list3.index(123))
print(list4)
list4.reverse()
print(list4)

list5 = [1,5,6,2,6,7,7,3,43,56]
list5.sort()
print(list5)