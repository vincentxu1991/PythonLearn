"""
    else 语句
        1,要么xx,要么yy
        2,干完了就能xx,干不完就别想xx:
            配合while循环;如果循环体中的内容全部执行完毕,则执行else,如果循环体使用break跳出,则不执行else
        3,没问题,开搞
            配合异常处理;只要try语句块中没有出现异常,就会执行else中的内容
            
    with 语句:
        抽象出频繁使用try..except...finally..语句,对文件使用
    
"""

try:
    int('abc')
    int('123')
except ValueError as reason:
    print('错误', reason)
else:
    print('ok')


try:
    with open('data.txt') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('error!', reason)



