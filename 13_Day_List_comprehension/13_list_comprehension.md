
[<< Day 12](../12_Day_Modules/12_modules.md) | [Day 14>>](../14_Day_Higher_order_functions/14_higher_order_functions.md)


- [📘 Day 13](#-day-13)
  - [列表推导式](#列表推导式)
  - [Lambda函数](#lambda函数)
    - [创建Lambda函数](#创建lambda函数)
    - [在另一个函数中使用lambda](#在另一个函数中使用lambda)
  - [💻 第13天练习](#-第13天练习)

# 📘 Day 13

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## 列表推导式

在Python中，列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。一种从序列创建列表的紧凑方式。列表推导式比使用 _for_ 循环处理列表要快得多。

```py
# 语法形式
[i for i in iterable if expression]
```
它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是 0 个或多个 for 或者 if 语句。简单来讲，是从第一个for开始依次向右推导，得出结果后给到最左边第一个变量。

**基础实例1：**

如果你想将字符串转换为字符列表。你可以使用一些方法。让我们来看看其中的一些:

```py
# 方式一
language = 'Python'
lst = list(language) # 将字符串更改为list
print(type(lst))     # <type 'list'>
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# 方式二: 列表推导式
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**基础实例2：**

例如，如果你想生成一个数字列表。

```py
# 生成数列
numbers = [i for i in range(11)]  # 生成0到10的数字
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 在迭代过程中可以进行数学运算
squares = [i * i for i in range(11)]
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 也可以创建一个元组列表
numbers = [(i, i * i) for i in range(11)]
print(numbers)  #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

```
为了更好的理解，我将上边的数学运算推导转换成普通的方式，通过对比或许帮助你理解其中逻辑
```py
squares = []
for i in range(11):
  compute = i * i
  squares.append(compute)

print(squares)
```

**实例3：带条件**

列表推导式可以与 _if_ 表达式结合使用

```py
# 奇数列表
even_numbers = [i for i in range(21) if i % 2 == 0]  # 生成范围为0到21的偶数列表
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 偶数列表
odd_numbers = [i for i in range(21) if i % 2 != 0]  # 生成范围为0到21的奇数列表
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 过滤数字：可以从下面的列表中过滤出正偶数
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 将二维数组合并成一维数组
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
因为带条件稍微复杂了点，因此我将上边后三个例子进行顺序拆解，让我们看看是啥样:
```py
# 偶数列表
even_numbers = []
for i in range(21):
    if i % 2 != 0:
        even_numbers.append(i)
print(even_numbers)

# 过滤出正整数
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = []
for i in range(21):
    if i % 2 == 0 and i > 0:
        positive_even_numbers.append(i)
print(positive_even_numbers) 

# 将二维数组合并成一维数组
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = []
for row in list_of_lists:
    for number in row:
        flattened_list.append(number)
print(flattened_list)
```
我想经过的拆解对比，应该对于列表的推导有一定了解了。这也算在学习Python路上接触的第一个所谓的语法糖了。是不是一下子就高级起来了。但需要提醒的是，如果你对这逻辑无法理解或不能熟练应用。建议还是老老实实写普通方法实现。

## Lambda函数

Lambda函数是一个没有名字的小型匿名函数。它可以接受任意数量的参数，但只能有一个表达式。Lambda函数类似于JavaScript中的匿名函数。当我们想在另一个函数里面写一个匿名函数时，我们就需要它。

### 创建Lambda函数

要创建lambda函数，我们使用 _lambda_ 关键字后跟一个形参和表达式。请参阅下面的语法和示例。Lambda函数不使用 return，它显式地返回表达式。

```py
# 语法
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

**例子**

```py
# 1.函数命名
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))   # 5

# 2.让我们把上面的函数换成 lambda 
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# 3.自调用 lambda 函数(将2中进一步简化)
print((lambda a, b: a + b)(2,3)) # 5 - 需要将其封装在print()中，以便在控制台中查看结果

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# 多变量
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### 在另一个函数中使用lambda

我们可以直接在一个函数里直接使用lambda表达式。具体举一个例子：

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # 函数power在括号需求两个参数来运行
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

可能有些晦涩难懂。这里同样进行拆解说明：

1. 当调用power函数的时候先将第一个参数2赋值给 x
2. x参数值传递给lambda表达式即 lambda n：2 ** n 并返回这个匿名函数
3. 紧接着将第二个参数5赋值给匿名函数参数 n
4. 匿名lambda进行表达式计算 2 ** 3 算的结果
5. 将最终两次函数逻辑结果赋值给cube变量，最后通过print打印结果为 8

```py
# 如果将上边嵌套匿名函数用普通函数嵌套表示可转化为：
def power(x, n):
    def inner(n):
        return x ** n
    return inner(n)

cube = power(2,3) 
print(cube)
```
以上就是本节一些在python语法中高级的用法学习。希望多多体会，当然这一开始就说如果你对这不熟悉请回归到最基本的编程方法上。


🌕 再接再厉。保持前进的势头，天空才是极限！你刚刚完成了第13天的挑战，和以往一样让我们做一些联系巩固学习成功吧。

## 💻 第13天练习

1. 使用列表推导式过滤出列表中零和负数
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. 利用推导式将下边的多维数组变成一维数组:

   ```py
   list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

   # 输出
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. 使用列表推导式创建以下元组列表:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. 将countries元组列表转换成目标输出列表:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

   # 输出:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
5. 将下面的列表更改为字典列表:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   
   # 输出:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
6. 将下面的列表列表更改为连接字符串的列表:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   # 输出
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
7. 编写一个lambda函数，它能够解决线性函数的斜率计算。

🎉 CONGRATULATIONS ! 🎉

[<< Day 12](../12_Day_Modules/12_modules.md) | [Day 14>>](../14_Day_Higher_order_functions/14_higher_order_functions.md)
