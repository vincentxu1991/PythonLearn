"""
    异常:
        try:
            语句块
        :except Exception[as reason]:
            异常处理代码
        finally:
            无论如何都需要执行
            
    :raise语句:
        引发一个异常
"""

# file_name = input("请输入文件名: ")
# f = open(file_name)
# print("文件的内容是: ")
# for each_line in f:
#     print(each_line)
#
# my_list = ['许大然是客服']
# assert len(my_list) > 0

try:
    int('abc')
    sum = 1+'1'
    f = open('hi.txt')
    words = f.read()
    f.close()
except OSError as reason:
    print('文件名输入错误', str(reason))
except TypeError as reason:
    print('类型出错:',reason)

except ValueError as reason:
    print("值错误", reason)


try:
    int('abc')
    sum = 1+'1'
    f = open('hi.txt')
    words = f.read()
    f.close()
except (OSError, TypeError, ValueError):
    print("错误")


raise ZeroDivisionError("除数为0")

