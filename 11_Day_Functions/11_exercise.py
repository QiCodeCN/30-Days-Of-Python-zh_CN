# 练习 1.1 声明一个函数名为 add_two_numbers。它接收两个数字参数，然后经过求和计算返回其值
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


print("求和2 + 3 =", add_two_numbers(2, 3))


# 练习 1.2 圆的面积的计算方法如下：Area = π x r x r。写一个函数计算 area_of_circle
def area_of_circle(r):
    pi = 3.14
    return pi * r * r


print("半径为2的圆面积：", area_of_circle(2))


# 练习 1.3 编写一个名为 add_all_nums 的函数，它接受任意数量的参数并对所有参数求和。要求检查是否所有列表项都是数字类型。如果没有则需要给出合适返回提示。
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total


print("任意参数求和：", add_all_nums(1, 2, 3, 4, 5))


# 练习 1.4 摄氏度°C可以转换为华氏度°F，使用以下公式为 °F =(°C x 9/5) + 32。写一个函数将°C转换为°F, 此函数名为 convert_celsius_to_fahrenheit
def convert_celsius_to_fahrenheit(c_value):
    f_value = c_value * 9 / 5 + 32
    return f_value


print("°F = ", convert_celsius_to_fahrenheit(10))


#  练习 1.5 编写一个名为 check_season 的函数，它接受一个月份参数并返回其对应的季节：秋季、冬季、春季或夏季
def check_season(month):
    if month in [1, 2, 3]:
        return "春季"
    elif month >= 4 and month <= 6:
        return "夏季"
    elif month == 7 or month == 8 or month == 9:
        return "秋季"
    else:
        return "冬季"


month = 7
print(f"{month}月属于：", check_season(month))


# 练习 1.6 声明一个名为 print_list 的函数。它接受一个列表作为参数，并输出列表中的每个元素
def print_list(items):
    print("列表打印：")
    for item in items:
        print(item)


print_list(["item1", "item2", "item3"])


# 练习 1.7 声明一个名为 reverse_list 的函数。它接受一个数组作为参数，并返回数组的反向(使用循环)
def reverse_list(flist):
    length = len(flist)
    rlist = []
    while length > 0:
        length = length - 1
        rlist.append(flist[length])
    return rlist


print("列表倒叙1：", reverse_list([1, 2, 3, 4, 5]))
print("列表倒叙2：", reverse_list(["A", "B", "C"]))


# 练习 1.8 声明一个名为 capitalize_list_items 的函数。它接受一个列表作为参数，并返回一个大写的项目列表
def capitalize_list_items(input_list):
    capital_list = []
    for item in input_list:
        capital_list.append(str(item).capitalize())
    return capital_list


print("小写转大写：", capitalize_list_items(["a", "c", "e"]))


# 练习 1.9 声明一个名为 add_item 的函数。它接受一个列表和一个实参数。它返回一个末尾添加了项目的列表
def add_item(items, item):
    # return items + [item]
    items.append(item)
    return items


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


# 练习 1.10 声明一个名为 remove_item 的函数。它接受一个列表和一个项参数。它返回一个删除了项目的列表
def remove_item(items, item):
    items.remove(item)
    return items


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


# 练习 1.11 声明一个名为 sum_all_numbers 的函数。它接受一个number参数并将该范围内的所有数字相加
def sum_all_numbers(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i
    return sum


print("5范围内数和：", sum_all_numbers(5))
print("10范围内数和：", sum_all_numbers(10))
print("100范围内数和：", sum_all_numbers(100))


# 练习 1.12 声明一个名为 sum_of_odds 的函数。它接受一个数字参数，并将该范围内的所有奇数相加
def sum_of_odds(num):
    sum = 0
    for i in range(1, num + 1):
        if i % 2 == 1:
            sum = sum + i
    return sum


print("所有奇数相加：", sum_of_odds(5))


# 练习 1.13 声明一个名为 sum_of_even 的函数。它接受一个数字参数，并将该范围内的所有偶数相加
def sum_of_even(num):
    sum = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            sum = sum + i
    return sum


print("所有偶数相加：", sum_of_even(5))


# 练习 2.1 声明一个名为 evens_and_odds 的函数。它取一个正整数作为参数，计算数字中偶数和奇数的个数
def evens_and_odds(num):
    i = 1  # 正整数不包括零
    odds_count = 0
    even_count = 0
    while i <= num:
        if i % 2 == 0:
            even_count += 1
        else:
            odds_count += 1
        i = i + 1
    return even_count, odds_count


event, odds = evens_and_odds(100)
print("奇数的个数是", event)
print("偶数的个数是", odds)


# 练习 2.2 调用函数 factorial ，它接受一个整数作为参数并返回这个数的阶乘
def factorial(num):
    calculate = 1
    for i in range(2, num + 1):
        calculate = calculate * i
    return calculate


test_num = 5
print(f"{test_num}的阶乘:", factorial(test_num))


# 练习 2.3 调用自定义函数 is_empty，它接受一个参数并检查它是否为空
def is_empty(obj):
    # 因为题目中未指明具体类型，所以仅举例几个类型做为判断，实际的应用一般都会预期的类型
    if type(obj) is str:
        return obj == ''
    elif type(obj) == list:
        return len(obj) == 0
    elif type(obj) == int:
        return obj == 0
    else:
        return "未支持的类型"


print("对象是否为空:", is_empty(''))
print("对象是否为空:", is_empty('python'))
print("对象是否为空:", is_empty([]))
print("对象是否为空:", is_empty([1, 2, 3]))
print("对象是否为空:", is_empty(1.22))


# 练习 3.1 编写一个名为 is_prime 的函数，它检查一个数字是否是素数
def is_prime(num):
    # 素数又叫质数，指的是大于1的整数中，只能被1和这个数本身整除的数。
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("1是否为素数:", is_prime(1))
print("9是否为素数:", is_prime(9))
print("11是否为素数:", is_prime(11))

# 练习 3.2 编写一个函数来检查列表中是否所有项都是唯一
def is_unique(items):
    # 方式一: 循环用list内置count统计
    # for item in items:
    #     if items.count(item) > 1:
    #         return False
    # return True

    # 方式二: 利用set不去重
    if len(items) == len(set(items)):
        return True
    else:
        return False


print("检查列表是否唯一", is_unique([1, 2, 3, 4, 5, 6]))
print("检查列表是否唯一", is_unique([1, 2, 3, 4, 3, 6]))


# 练习 3.3 编写一个函数来检查列表中的所有项是否都是相同的数据类型
def is_same_type(ls):
    type_mark = type(ls[0])
    for i in range(1, len(ls)):
        if type_mark is not type(ls[i]):
            return False
    return True


print("检查是否均为同类型", is_same_type([1, 2, 3, 4, 5]))
print("检查是否均为同类型", is_same_type([1, 2, "test", 0.2]))
print("检查是否均为同类型", is_same_type(['Beijing', "Shanghai", "Shenzhen"]))