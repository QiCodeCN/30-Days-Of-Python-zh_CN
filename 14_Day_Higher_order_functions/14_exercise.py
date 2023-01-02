# 练习1级 - 基础回顾知识点 略 -

# 2.1 使用 map 实现countries列表中项全部转大写，然后返回一个新的列表并打印
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def change_upper(country):
    return country.upper()
upper_countries = list(map(change_upper, countries))
print(upper_countries)

# 2.2 使用 map 实现numbers列表中的平方计算，并返回新的列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def calculate_square(num):
    return num * num
squares = list(map(calculate_square, numbers))
print(squares)  

# 2.3 使用 map 将names列表转大写
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))

# 2.4 使用 filter 过滤掉 countries 列表中含有 land 关键词的国家
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
filter_countries = filter(lambda name: 'land' not in name, countries)
list_country = list(filter_countries)
print("原国家数据：", countries)
print("去除含land的数据：", list_country)

# 2.5 使用 filter 过滤出 countries 列表中项字符串长度正好是6个的国家
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def len_six(country):
    if len(country) == 6:
        return True
    return False
six_countries = filter(len_six, countries)
print("长度等于6的新列表：", list(six_countries))

# 2.6 使用 filter 过滤出 countries 列表中国家字符长度大于6个项
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
more_six_list = list(filter(lambda c: len(c)>6, countries))
print("字符大于6的国家：",more_six_list)

# 2.7 使用 filter 过滤出 countries 列表中项以字符 E 开头的国家
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def start_e(country):
    if country.startswith('E'):
        return True
    return False
e_countries = filter(start_e, countries)
print("字符E开头的国:", list(e_countries))

# 2.8 练习使用两个或多个方法内置高阶函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def map_square(num):
    return num ** 2

def filter_even(num):
    if num % 2 == 0:
        return True
    return False

chain = filter(filter_even,  list(map(map_square, numbers)))
print("连续使用多个高阶内置函数：", list(chain))

# 2.9 声明一个名为 get_string_lists 的函数，该函数接受一个列表作为参数，然后返回一个仅包含字符串项的列表
def get_string_lists(item):
    if type(item) is str:
        return True
    return False
print("过滤字符串列表：", list(filter(get_string_lists, [1, "Maga", "2", 3, "Qi", 4])))

# 2.10 使用 reduce 对 numbers 列表中的所有数字求和
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("列表求和：", reduce(lambda x, y: x+y, numbers))

# 2.11 用 reduce 将所有的国家连在一起，最终形成句子：爱沙尼亚、芬兰、瑞典、丹麦、挪威和冰岛都是北欧国家
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def join_country(c1, c2):
    return f'{c1}、{c2}'
link_country = reduce(join_country, countries) + ' is Nordic countries'
print("集合国家：", link_country)

# 3.1 按国家名称、首都和人口数量对其进行排序
import os
import json

path_data = os.getcwd() + "\data\countries_data.json"  # 配置数据文件路径

with open(path_data, mode='r') as f:  #  打开文件并用json加载数据
    countries = json.load(f)

# print(sorted(countries, key=lambda item: item['name'], reverse=True)) # 利用内置高阶函数sorted根据每一项单按名字排序
print(sorted(countries, key=lambda c: (c['name'], c['capital'], c['population'])))  # 多关键词依次排序

# 3.2 选出十个人口最多的国家
population_sort = sorted(countries, key=lambda item: item['population'], reverse=True) # 先按人口关键词大-小排序
print("人口最多前十国家：",[country["name"] for country in population_sort[:10]]) # 分片取出前十，再用列表推导式取出国家名字
