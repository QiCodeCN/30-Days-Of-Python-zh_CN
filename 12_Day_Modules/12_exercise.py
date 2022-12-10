from modules import *

# 练习 1.1 编写一个 random_user_id 函数，它的功能是随机生成6位字符（包括字母和数字）
print("随机生成6位用户ID：", random_user_id())

# 练习 1.2 声明一个名为 user_id_gen_by_user 的函数。它不设置参数，但它使用input() 接受两个输入。其中一个输入是字符的数量，第二个输入是应该生成的id的数量
# user_ids = user_id_gen_by_user()
# for user_id in user_ids:
#     print(user_id)

# 练习1.3 编写一个名为 rgb_color_gen 函数。它将生成rgb颜色(3个值，每个值从0到255)
print("rgb随机颜色：", rgb_color_gen())


# 练习2.1 编写一个函数 list_of_hexa_colors，它返回数组中任意数量的十六进制颜色(在#之后写入的六个十六进制数)。十六进制数字系统由16个符号组成，0-9和字母表的前6个字母a-f
print("返回两组HEXA颜色：", list_of_hexa_colors(2))

# 练习2.2 编写一个函数 list_of_rgb_colors，它返回任意数量的RGB颜色数组。
print("返回两组RGB颜色：", list_of_rgb_colors(2))

# 练习2.3 写一个函数 generate_colors，它可以生成任意数量的hexa或rgb颜色
print("hexa,3：", generate_colors('hexa', 3))
print("hexa,1：", generate_colors('hexa', 1))
print("rgb,3：", generate_colors('rgb', 3))
print("rgb,1：", generate_colors('rgb', 1))

# 练习3.1 调用你的编写的函数 shuffle_list，它接受一个列表作为参数，并返回一个打乱的列表
original_list = [1, 2, 3, 4, 5, 6]
print("初始顺序：", original_list)
print("打乱后顺序：", shuffle_list(original_list))

# 练习3.2 编写一个函数，返回由0-9范围内的7个随机数组成的数组。所有的数字必须是唯一的
print("随机7位唯一数列表：", random_seven_number())