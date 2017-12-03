"""
元组:元祖是不可改变的类型
    元组的标致性:逗号
    

"""

tuple1 = (1, 2, 3, 4, 5, 6)

tuple2 = (1)
print(type(tuple2))

tuple3 = 2, 3, 4, 5, 6
print(type(tuple3))

tuple4 = 2,
print(type(tuple4))

temp = ('上海', '北京', '广州')
print(temp)
temp = temp[:2] +('太原',) +temp[2:]
print(temp)