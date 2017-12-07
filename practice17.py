"""
    输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
str1 = input('请输入一个字符串: ')
if len(str1) == 0 :
    print("error")
else:
    num = 0
    space = 0
    alpha = 0
    others = 0
    for i in str1:
        if i.isnumeric():
            num += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            others += 1
    print("数字数量:%d;字母数量:%d;空格数量:%d;其他:%d." % (num, alpha, space, others))


