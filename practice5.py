"""
    输入三个整数x,y,z，请把这三个数由小到大输出。
"""

l = []
for i in range(1,4):
    x = int(input("请输入数字:"))
    l.append(x)
l.sort()
print(l)
