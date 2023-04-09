# Python中的算数运算
# 整数

print('加法Addition: ', 1 + 2)          # 3
print('减法Subtraction: ', 2 - 1)       # 1
print('求幂miMultiplication: ', 2 * 3)  # 6

# 在Python中除法得到结果是浮点类型
print('除法Division: ', 4 / 2)       # 2.0  
print('除法Division: ', 7 / 2)        # 3.5
print('求商: ', 7 // 2)               # 3
print('Division without the remainder: ',7 // 3)   # 2
print('求余Modulus: ', 3 % 2)         # 1
print('幂: ', 2 ** 3) # 8， 可理解为 2 * 2 * 2

# 浮点数
print('PI', 3.14)
print('gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# 首先在顶部声明变量

a = 3 # a是变量名，3是整数
b = 2 # b是变量名，2是整数

# 进行运算并将结果赋值给新的变量
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# 总数表示本应该用sum，但是它是pyhon的关键词，为了避免重复用了total代替
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# 声明变量值，并将他们进行组合运算
num_one = 3
num_two = 4

# 算术运算
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# 打印计算后并赋值给新变量的值
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# 计算圆的面积
radius = 10                                 # 圆的半径
area_of_circle = 3.14 * radius ** 2         # 两个星(**)表示指数
print('Area of a circle:', area_of_circle)

# 计算矩形的面积
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# 计算物体的重量
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# 计算液体的密度
mass = 75 # KG
volume = 0.075 # 立方米
density = mass / volume # 1000 Kg/m^3


print(3 > 2)     # True, 因为 3 大于 2
print(3 >= 2)    # True, 因为 3 大于 2
print(3 < 2)     # False,  因为 3 大于 2
print(2 < 3)     # True, 因为 2 小于 3
print(2 <= 3)    # True, 因为 2 小于 3
print(3 == 2)    # False, 因为 3 不等于 2
print(3 != 2)    # True, 因为 3 确实不等于 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# 比较两个对象并给出值
print('True == True: ', True == True)    # True
print('True == False: ', True == False)  # False
print('False == False:', False == False) # True

print('1 is 1', 1 is 1)                   # True 
# 第一条 如果python shell 中运行此条会有个警告 （下面数值比较也类似）
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
# 忽略即可，也就是值比较的时候建议用==

print('1 is not 2', 1 is not 2)           # True
print('M in MegaQi', 'M' in 'MegaQi') # True
print('B in MegaQi', 'B' in 'MegaQi') # False 
print('coding' in 'coding for all') # True
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - 因为两个比较结果都是True
print(3 > 2 and 4 < 3) # False - 因为第二比较为False
print(3 < 2 and 4 < 3) # False - 因为两个比较都为False
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - 因为两个比较结果都是True
print(3 > 2 or 4 < 3)  # True - 因为第一个表述为真
print(3 < 2 or 4 < 3)  # False - 因为两个比较表述都为假
print('True or False:', True or False)
print(not 3 > 2)     # False - 因为 3 > 2 是 true, 然后 True 反向为 False
print(not True)      # False - 反转操作  不为 true 则 false
print(not False)     # True
print(not not True)  # True
print(not not False) # False