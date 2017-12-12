"""
    汉诺塔
        递归求解汉诺塔
"""

# 将n个盘子移动到z
def hanoi(n, x='x', y='y', z='z'):
    if(n == 1):
        print(x, '->', z)
    else:
        hanoi(n-1, x, z, y)# 将前n-1的盘子从x移动到y上
        print(x, '->', z) # 将最底下的最后一个盘子从x移动到z上
        hanoi(n-1, y, x, z)
n = int(input("请输入汉诺塔层数: "))
hanoi(n)




