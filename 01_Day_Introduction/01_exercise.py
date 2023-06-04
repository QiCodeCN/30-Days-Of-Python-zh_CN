# 1.1 - 1.3 在python shell上操作略..

# 1.4 检查数据类型
print(type(10))                    # int
print(type(9.8))                   # float
print(type(3.14))                  # float
print(type(5-5j))                  # complex
print(type(['Python', 'Java']))    # list
print(type((1,2,3)))               # tuple
print(type("China"))               # str

# 2.1 在 helloworld.py 文件中再次练习1中的所有题目
# 参考 helloworld.py


# 3.1 python数据类型
print('Integer:', 10)
print('Float:', 3.14)
print('Complex:', 3+3j)
print("String:", 'Hello World!')
print('Boolean:', True)
print('List:', [1,3,'五',7,9])
print('Tuple:', (2,4,6))
print('Set:', {8,9,10})
print('Dictionary:',{'name':'MegaQi', '公众号':'非典型性程序员'})

# 3.2 计算两点之间距离
'''
 几何数学计算，可以描绘为在x和y轴两点画斜线，在做两个垂直直线。即又勾股定理计算
 因为还没有学后边关于变量只是，如果是零基础同学，可以直接计算实现 **0.5 相当于开平方
 注意这里计算完默认打印出来的是浮点类型
'''
print(((6-2)*(6-2) + (6-3)*(6-3))**0.5)

# 如果后边学了变量, 类型操作和一些函数方法可以按如下写(切记：此参考零基础同学千万别纠结要一下弄懂，后边都会学到)
import math
point1 = (2, 3)
point2 = (6, 6)
x = point2[0] - point1[0]
y = point2[1] - point1[1]
distance = math.sqrt(x**2 + y**2)
print("两点间距离：", distance)

print(1,2,2)
print({1,2,2,2})
print({"1":1,"1":2})