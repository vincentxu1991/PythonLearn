# 三元操作符
# small = x if x<y else y
""""
assert 断言:一般用在测试的情况下

for循环:
for 目标 in 表达式:
    循环体
    
range()函数 range([start,],stop[,step=1])
生成一个从start参数值开始到stop参数值结束的数字序列

"""

# assert 3 > 4
# assert 3 < 4

fav = 'Vincent'
for i in fav:
    print(i, end=' ')

print('\n')
member =['vincent','大佬','黑夜','白天','添加']
for j in member:
    print(j, len(j))

print(('\n'))
print(range(5))
print(list(range(5)))

for each in range(5):
    print(each)
print('\n')
for each in range(2,9):
    print(each)

print('\n')
for each in range(2,9,3):
    print(each)
