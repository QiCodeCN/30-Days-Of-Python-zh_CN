#
import string
import random


def random_user_id():
    '''
    随机生成6位字符（包括字母和数字）
    :return: 6位ID
    '''
    lowercase_and_number = string.ascii_lowercase + string.digits
    six_id = ""
    for i in range(6):
        index = random.randint(0, len(lowercase_and_number) - 1)
        six_id = six_id + lowercase_and_number[index]
    return six_id


def user_id_gen_by_user():
    '''
    获取用户给定两个数生成对应数量的用户ID
    :return: 用户ID列表
    '''
    str_num = int(input("输入字符数量："))
    id_num = int(input("输入生成的ID数量："))
    letters_and_number = string.ascii_letters + string.digits
    user_id_list = []
    for i in range(id_num):
        user_id = ""
        for s in range(str_num):
            index = random.randint(0, len(letters_and_number) - 1)
            user_id = user_id + letters_and_number[index]
        user_id_list.append(user_id)
    return user_id_list


def rgb_color_gen():
    '''
    生成一个RGB颜色
    :return: 三位数RGB元组
    '''
    items = list()
    for i in range(3):
        item = random.randint(0, 255)
        items.append(item)

    rgb = tuple(items)
    return rgb


def list_of_hexa_colors(number):
    '''
    生成指定数量的16进制的颜色组
    :param number: 数量
    :return: hexa颜色组
    '''
    color_charts = ['a', 'b', 'c', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    hexa_list = []
    for i in range(number):
        num = 0
        hexa_color = '#'
        while num < 6:
            index = random.randint(0, len(color_charts) - 1)
            hexa_color = hexa_color + color_charts[index]
            num += 1
        hexa_list.append(hexa_color)

    return hexa_list


def list_of_rgb_colors(number):
    '''
    生成指定数量的RGB颜色组，并且格式化为rgb(106,227,72)
    :param number: 数量
    :return: rgb颜色组
    '''
    rgb_list = []

    for num in range(number):
        item = 0
        rgb = "rgb("
        while True:
            rgb = rgb + str(random.randint(0, 255))
            item += 1
            if item < 3:
                rgb = rgb + ','
            else:
                break
        rgb = rgb + ")"
        rgb_list.append(rgb)

    return rgb_list


def generate_colors(color_type, number):
    '''
    按照指定类型返回数组颜色
    :param color_type: 颜色类型
    :param number: 颜色数量
    :return: 颜色组
    '''
    if color_type == 'hexa':
        return list_of_hexa_colors(number)
    elif color_type == 'rgb':
        return list_of_rgb_colors(number)

def shuffle_list(input_list):
    '''
    使用random内置函数直接返回打乱顺序的列表
    :param input_list:
    :return: 列表
    '''
    tmp_list = input_list
    random.shuffle(tmp_list)
    return tmp_list

def random_seven_number():
    '''
    利用random内置函数sample，从一个总体序列或集合中选择k个唯一的随机元素。
    :return:
    '''
    numbers = list(range(0, 10))
    unique_items = random.sample(numbers, 7)
    return unique_items
