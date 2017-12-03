"""
字符串的内置方法:
    capitalize()第一个字符大写
    center(x)居中,左边右边各空出x个位置
    count(sub[,start,end])统计字符串出现的次数
    encode(encoding = 'utf-8',errors='strict')更改编码
    endswith(sub[,start,end])是否已字符串sub结尾
    isalnum()判断字符串是否只存在字母和数字,
    isalpha()判断字符串是否只包含字母
    isdecimal()判断字符串中是否只包含十进制的数字
    isdigit()判断字符串是否只包含数字
    islower()判断字符串中所有字符是否为小写
    isnumeric()判断字符串中是否只包含数字字符
    isspace()判断字符串中是否只包含空格
    istitle()判断字符串是否标题化(所有单词都是以大写开头,其余字母为小写)
    isupper()判断字符串中的字母全为大写
    join(sub)以字符串作为分隔符,插入到sub中所有的字符之间
    ljust(x)左对齐
    low()将字符串转换为全部小写
    lstrip()去掉字符串左边的全部空格
    partition(sub)找到sub,将字符串分成三个元组(pre_sub,sub,fol_sub)
    replace(old,new,[count])将new替换成old,不超过count次
    split(sep=none,maxsplit=1)按照空格来切字符串,返回一个列表
    splitlines(([keepends]))按照'\n'分隔,返回列表
    strip([chars])默认删除字符串前后空格,中间空格不删,若给参数,则去除参数
    title()返回标题化的字符串
    translate(table)根据table的规则(可以由str.maketrans('a', 'b')定制)转换字符串中的字符
    zfill(width)返回长度为width的字符串,原字符串右对齐,前面用0填充
    
"""

str1 = 'abcdefg'
print(str1[:6])
print(str1[1])
print(str1[:6] + "插入的字符串" +str1[6:])
str2 ='xiaoxie'

print(str2.capitalize())
str3 = 'DAXIE'
print(str3.center(40))
print(str3.count('xi'))
print(str2.count('xi'))
print(str3.endswith('xi'))
print(str2.endswith('xie'))

str4 = 'VincenT'

print(str4)
print(str4.join('1234'))

str5 = 'tianganwuzao,xiaoxinhuozhu'
print(str5.partition('ao'))

print(str5.translate(str.maketrans('o','v')))
print(str.maketrans('o','v'))