# 1.使用列表推导式过滤出列表中零和负数
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_list = [i for i in numbers if i <= 0]
print(filter_list)

# 2.利用推导式将下边的多维数组变成一维数组
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_list = [one for three in list_of_lists for two in three for one in two ]
print(one_list)

# 3.使用列表推导式创建以下元组列表
tuple_list = [(i,1,i*1,i**2,i**3,i**4,i**5) for i in range(11)]
print(tuple_list)

# 4.将countries元组列表转换成目标输出列表
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
format1 = [[inlist[0][0].upper(), inlist[0][0].upper()[0:3], inlist[0][1].upper()] for inlist in countries]
format2 = [[tc[0].upper(), tc[0].upper()[:3], tc[1].upper()] for lc in countries for tc in lc]
print(format1)
print(format2)

# 5.将下面的列表更改为字典列表
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'contry': tc[0][0].upper(), 'city':tc[0][1].upper()} for tc in countries]
print(dict_countries)

# 6.将下面的列表列表更改为连接字符串的列表
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
format_names = [f'{tc[0]} {tc[1]}' for lc in names for tc in lc]
print(format_names)

# 7.编写一个lambda函数，求两点直线斜率
slope = lambda p1, p2 : (p2[1] - p1[1]) / (p2[0] - p1[0])
print(slope((1,1), (3,4)))
