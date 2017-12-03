"""
列表:打了激素的数组
往列表中添加元素:
    append()方法添加列表,参数为插入列表的元素
    extend([])扩张方法,可以添加另外一个列表,参数是一个列表
    insert(位置, 插入元素的值)方法

获得列表中的元素:    
    index方法获得列表中的元素

删除列表中的元素:    
    remove()方法,删除元素
    del语句
    pop()方法,从列表中取出最后一个元素并返回
    
切片(获取列表中的多个元素,以列表的形式返回):
    


"""
# 创建普通列表
member = ["上海", "北京", "广州"]
print(member)

# 创建混合类型的列表
mix = [1, "上海", "3.14", ["北京", "广州"]]
print(mix)

# 创建空列表
empty = []
print(empty)

member.append('新疆')
member.extend(['吉林', '重庆'])
print(member)
member.insert(1, '太原')
print(member)

print(member[0])
temp = member[0]
member[0] = member[1]
member[1] = temp
print(member)

member.remove('重庆')
print(member)

del member[0]
print(member)

member.pop()
print(member)

new_city = member.pop(1)
print(new_city)

print(member)
print(member[1:3])
print(member[:2])
print(member[:])