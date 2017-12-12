"""
    字典:当索引不好用时使用,映射类型
    {key:value}
"""

brand = ['李宁', '耐克', '阿迪达斯', '安踏']
slogan = ['一切皆有可能', 'just do it', 'impossible is nothing', '永不止步']
print('安踏的广告是:', slogan[3])
print('阿迪达斯的广告是:', slogan[brand.index('阿迪达斯')])
dict1 = {'李宁': '一切皆有可能', '耐克': 'just do it', '阿迪达斯': 'impossible is nothing', '安踏': '永不止步'}
print('耐克的口号是:', dict1['耐克'])


dict3 = dict(((1, 'one'), (2, 'two'), (3, 'three')))
print(dict3)

dict4 = dict(上海='哦,天呐', 天津='哦,上啊')
print(dict4)
dict4['北京'] = '皇城根'
dict4['天津'] = '狗不理'
print(dict4)
