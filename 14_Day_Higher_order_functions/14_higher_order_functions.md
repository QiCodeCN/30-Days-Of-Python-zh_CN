
> 目 录
- [📘 Day 14](#-day-14)
  - [高阶函数](#高阶函数)
    - [函数作为参数](#函数作为参数)
    - [函数作为返回值](#函数作为返回值)
  - [Python闭包](#Python闭包)
  - [Python装饰器](#Python装饰器)
    - [创建装饰器](#创建装饰器)
    - [某个函数加上多个装饰器](#某个函数加上多个装饰器)
    - [装饰器带参数](#装饰器带参数)
  - [内置高阶函数](#内置高阶函数)
    - [Python-Map](#python-map)
    - [Python-Filter](#python-filter)
    - [Python-Reduce](#python-reduce)
  - [💻 第14天练习](#-第14天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)
    - [练习3级](#练习3级)

# 📘 Day 14

## 高阶函数

在Python中，函数被视为第一类公民，允许对函数执行以下操作：

- 一个函数可以被作为另一个函数的一或多个参数
- 一个函数可以被作为结果或另一个函数返回
- 一个函数可以被修改
- 一个函数可以赋值给一个变量

在本节中，我们将介绍如下内容：

1. 将函数作为一个参数
2. 将函数作为另外一个函数的返回值
3. 使用Python闭包和装饰器

### 函数作为参数

```py
def sum_numbers(nums):  # 正常函数
    return sum(nums)    # 利用内置函数返回列表和

def higher_order_function(f, lst):  # 高阶函数：函数作为另一个函数其中一个参数
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### 函数作为返回值

```py
def square(x):          # 平方函数
    return x ** 2

def cube(x):            # 立方函数
    return x ** 3

def absolute(x):        # 绝对值函数
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # 将函数作为返回值，声明一个高阶函数
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

从上面的例子中可以看到，高阶函数根据传递的参数返回不同计算函数，然后在进行最后赋值计算。

## Python闭包
Python允许嵌套一个函数，此函数可以访问外部函数的变量。这就是所谓的闭包。让我们看看闭包在Python中是如何工作的。在Python中，闭包是通过在另一个封装函数中嵌套一个函数，然后返回内部函数来创建的。请参阅下面的示例。

**例子:**

```py
def add_ten():
    ten = 10
    # 函数内部再定义一个函数
    def add(num):
        return num + ten
    # 将内部函数add作为返回值返回
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

回过头来引用下维基百科中更为严谨的定义：
> 在一些语言中，在函数中可以（嵌套）定义另一个函数时，如果内部的函数引用了外部的函数的变量，则可能产生闭包。闭包可以用来在一个函数与一组“私有”变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能够保持其持久性。

补充一下闭包在Python中的作用：
1. 读取函数内部的变量
2. 让函数内部的局部变量始终保持在内存中

## Python装饰器

装饰器是Python中的一种设计模式，本质上是一个Python函数(其实就是闭包)，允许用户在不修改现有对象结构的情况下向其添加新功能。装饰器通常在要装饰的函数定义之前调用。装饰器用于有以下场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。

### 创建装饰器

要创建一个装饰器，我们只需要在一个外部函数中封装一个内部函数即可。

**举例:**

```py
# 正常写法
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

# 用一个装饰器来实现上面的例子
'''这个装饰函数，它是一个高阶函数，它以一个函数作为参数'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator  # 通过@注解
def greeting():
    return 'Welcome to Python'

print(greeting())   # WELCOME TO PYTHON

```

### 某个函数加上多个装饰器

```py

'''这个装饰函数，它是一个高阶函数，
它以一个函数作为参数'''

# 第一个装饰器：字符转大写
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# 第二个装饰器：拆分字符串
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator     # 这里注意多个装饰的执行顺序：先执行在底部，这里为先转大写再拆分
def greeting():
    return 'Welcome to Python'

print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### 装饰器带参数
在大多数情况下，装饰器函数中也需要传递参数。因此我们可能需要定义一个接受参数的装饰器。

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Mega", "Qi",'China')

```

以上例子中先执行 print_full_name 方法中的打印，然后装饰器同步获得三个参数，并内部使仅使用的第三个参数进行了拼装打印。它的预期结果如下：

```shell
I am Mega Qi. I love to teach.
I live in China
```

## 内置高阶函数

本部分介绍的一些内置高阶函数，它们有 _map()_、_filter_和_reduce_。

Lambda函数可以作为参数传递，Lambda函数的最佳案例如：map、filter和reduce等函数。

### Python-Map

`map()` 函数是一个内置函数，它以函数和可迭代对象作为参数。

```py
# 语法
map(function, iterable)
```

**示例1：平方计算**

```py
numbers = [1, 2, 3, 4, 5] # iterable

def square(x):
    return x ** 2
    
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# 让我们将它应用到 lambda 匿名函数上
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**示例2：字符列表转整数**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)  # 将字符串列表迭代转成数字列表
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**示例3：转大写**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# lambda 匿名函数方式
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

实际 map 做的事情是迭代一个列表。例如（示例3）：它将名称更改为大写并返回一个新列表。

### Python-Filter
函数 `filter()` 调用指定的函数，该函数为指定的可迭代对象(列表)的每一项布尔值返回。即它过滤满足条件的项。

```py
# 语法形式
filter(function, iterable)
```

**示例1：返回偶数**

```py
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**示例2：返回奇数**

```py
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

**示例3：过滤长字符名字**
```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python-Reduce
函数 `reduce()` 会对参数序列中元素进行累积。是在 _functools_ 模块中定义的。我们要使用它需要从这个模块中导入。像map和filter一样，它有两个参数，一个函数参数和一个可迭代对象参数。但它不会返回另一个迭代对象，而是返回一个单独的值。

**示例1：**

```py
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5'] 
def add_two_nums(x, y):  # 两数相加
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str) # # 计算列表和：1+2+3+4+5
print(total)    # 15

# 使用 lambda 匿名函数
tota2 = reduce(lambda x, y: int(x)+int(y), numbers_str)  
print(total)    # 15
```

## 💻 第14天练习

练习原始值
```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### 练习1级

1. 解释下内置函数 _map_、_filter_ 和 _reduce_ 之间不同；
2. 解释高阶函数、闭包和装饰器之间的区别；
3. 参考知识点中的例子，使用 _map_ 、_filter_ 或 _reduce_ 自己做个练习；
4. 使用 for 循环打印 countries 列表中的每个国家；
5. 使用 for 打印 names 列表中的每个名字；
6. 使用 for 打印 numbers 列表中的每个数字。

### 练习2级

1. 使用 map 实现countries列表中项全部转大写，然后返回一个新的列表并打印；
2. 使用 map 实现numbers列表中的平方计算，并返回新的列表；
3. 使用 map 将names列表转大写
4. 使用 filter 过滤掉 countries 列表中含有 land 关键词的国家；
5. 使用 filter 过滤出 countries 列表中项字符串长度正好是6个的国家；
6. 使用 filter 过滤出 countries 列表中国家字符长度大于6个项；
7. 使用 filter 过滤出 countries 列表中项以字符 E 开头的国家；
8. 练习使用两个或多个方法内置高阶函数
9. 声明一个名为 _get_string_lists_ 的函数，该函数接受一个列表作为参数，然后返回一个仅包含字符串项的列表;
10. 使用 reduce 对 numbers 列表中的所有数字求和;
11. 用 reduce 将所有的国家连在一起，最终形成句子：爱沙尼亚、芬兰、瑞典、丹麦、挪威和冰岛都是北欧国家；

### 练习3级

1. 使用 countries_data.py (30-Days-Of-Python-zh_CN/data/countries_data.py) 文件完成如下任务：
    - 按国家名称、首都和人口数量对其进行排序
    - 选出十个人口最多的国家

🎉 CONGRATULATIONS ! 🎉

[<< Day 13](../13_Day_List_comprehension/13_list_comprehension.md) | [Day 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)