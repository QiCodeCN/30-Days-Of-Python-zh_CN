
[<< Day 10](../10_Day_Loops/10_loops.md) | [Day 12 >>](../12_Day_Modules/12_modules.md)


- [📘 Day 11](#-day-11)
  - [Functions函数](#Functions函数)
    - [定义函数](#定义函数)
    - [声明和调用](#声明和调用)
    - [无参函数](#无参函数)
    - [无参函数返回值](#无参函数返回值)
    - [带参函数](#带参函数)
    - [传递带键和值的参数](#传递带键和值的参数)
    - [有参函数返回值](#有参函数返回值)
    - [带默认参数的函数](#带默认参数的函数)
    - [任意参数函数](#任意参数函数)
    - [函数参数混合使用](#函数参数混合使用)
  - [💻 第11天练习](#-第11天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)
    - [练习3级](#练习3级)

# 📘 Day 11

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## Functions函数

到目前为止，我们已经看到了许多内置的Python函数。在本节中，我们将重点介绍自定义函数。 
什么是函数?在我们开始制作函数之前，让我们先了解一下什么是函数以及为什么需要函数?

### 定义函数

函数是为了执行特定任务而设计可重用代码块或编程语句。在Python要定义或声明一个函数，使用了def关键字。下面是定义函数的语法。只有在调用函数时才执行函数块内代码。

### 声明和调用

当我们创建一个函数时，我们将其称为声明函数。当我们开始使用它时，我们称之为调用（calling或invoking）函数。它的声明可以带形参，也可以不带形参。

```python
# 语法参考
# 声明一个函数
def function_name():
    codes

# 使用声明的函数
function_name()
```

### 无参函数

当函数声明的时候可以不带任何参数。

```python
# 实际例子
def generate_full_name ():
    first_name = 'Mega'
    last_name = 'Qi'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # 函数调用

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### 无参函数返回值

函数是可以有返回值的，如果函数没有返回语句，则函数的值为None。让我们使用return重写上面的函数。从现在开始，当我们调用函数并打印它时，我们从函数中获得一个返回值。
```python
def generate_full_name ():
    first_name = 'Mega'
    last_name = 'Qi'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### 带参函数

在函数中，我们可以将不同的数据类型(数字、字符串、布尔值、列表、元组、字典或集合)作为参数传递
- 单形参：如果函数接受一个参数，则调用函数时应附带一个实参
```  
# 语法形式参考
# 声明带一个参的函数
def function_name(parameter):
    codes

# 调用带参函数并给定参值
print(function_name(argument))
```

实际举例
```python
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('MegaQi')) # MegaQi, welcome to Python for Everyone!

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90)) # 100

def square_number(x):
    return x * x
print(square_number(2)) # 4

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10)) # 314.0

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

```
- 两个参数：一个函数可能无参或一个参数，也可能有多个参数。因此函数也可以有两个或多个形参。
```
# 语法形式：声明带两个参数的函数
def function_name(para1, para2):
    codes

# 调用函数并传两个参数
print(function_name(arg1, arg2))
```
实战例子
```python
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Mega','Qi'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2022, 1987))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # 将数值先转换成字符后再拼接
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

```

### 传递带键和值的参数

上方只传值的方式必须要严格遵守参数位置顺序。如果想不受限制可以传递带有key和value的参数。
```
# 使用语法
def function_name(para1, para2):
    codes

# 调用方法通过指定key=value
print(function_name(para1 = 'John', para2 = 'Doe'))
print(function_name(para2 = 'Doe', para1 = 'John'))
```
举例
```python
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_fullname(firstname = 'Mega', lastname = 'Qi'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

### 有参函数返回值

同无参数带返回值一样，有参函数也可以使用return返回函数值。以下举几个不同类型的返回例子。
- 返回一个字符串：
```python
def print_name(lastname):
    return lastname
print(print_name('Qi'))

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_full_name(firstname='Meage', lastname='Qi'))
```

- 返回一个数字
```python
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2022, 1987))
```

- 返回一个布尔值：
```python
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # Return停止函数的进一步执行，类似于break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- 返回一个列表
``` python
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### 带默认参数的函数

有时，在调用函数时，我们将默认值传递给参数。如果在调用函数时不传递实参，则使用它们的默认值。
```
# 语法形式：参数给定默认值
def function_name(param = value):
    codes

# 函数方法调用
function_name()
function_name(arg)
```

实战例子
```python
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Qi'))

def generate_full_name (first_name = 'Mega', last_name = 'Qi'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N'
    return weight
print('物体的重量（单位牛顿）: ', weight_of_object(100))
print('物体的重量（单位牛顿）: ', weight_of_object(100, 1.62))
```

### 任意参数函数

如果不知道传递给函数的实参数量，可以通过在形参名称前添加`*`来创建一个函数，该函数可以接受任意数量的实参。
```
# 语法形式 * 不确定参数
def function_name(*args):
    codes

# 调用方法传不定参数
function_name(param1, param2, param3,..)
```

实际例子
```python
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # 此计算方法等同于 total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### 函数参数混合使用
- 实参和不定参数

首参给定team，剩余其他以list形式给不定*args。但注意实参要在前面。否则会报 TypeError 错误。

```python

def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)

# 
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
```

- 函数作为另一个函数的参数
```python
# 可以将函数作为参数传递
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 到目前为止，你取得了很大的成就。继续前进！你刚刚完成了第11天的挑战，你向你的伟大之路前进了11步。现在检验下你的学习成功吧。


## 💻 第11天练习

### 练习1级

1. 声明一个函数名为 *add_two_numbers*。它接收两个数字参数，然后经过求和计算返回其值。
2. 圆的面积的计算方法如下:Area = π x r x r。写一个函数计算*area_of_circle*。
3. 编写一个名为add_all_nums的函数，它接受任意数量的参数并对所有参数求和。要求检查是否所有列表项都是数字类型。如果没有则需要给出合适返回提示。
4. 摄氏度°C可以转换为华氏度°F，使用以下公式为 °F =(°C x 9/5) + 32。写一个函数将°C转换为°F, 此函数名为*convert_celsius_to_fahrenheit*。
5. 编写一个名为*check_season*的函数，它接受一个月份参数并返回其对应的季节：秋季、冬季、春季或夏季。
6. 声明一个名为*print_list*的函数。它接受一个列表作为参数，并输出列表中的每个元素。
7. 声明一个名为reverse_list的函数。它接受一个数组作为参数，并返回数组的反向(使用循环)。
    ```
    print(reverse_list([1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]
    print(reverse_list(["A", "B", "C"]))
    # ["C", "B", "A"]
    ```
8. 声明一个名为*capitalize_list_items*的函数。它接受一个列表作为参数，并返回一个大写的项目列表。
9. 声明一个名为add_item的函数。它接受一个列表和一个实参数。它返回一个末尾添加了项目的列表。
    ```
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
    numbers = [2, 3, 7, 9];
    print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
    ```
10. 声明一个名为*remove_item*的函数。它接受一个列表和一个项参数。它返回一个删除了项目的列表。
    ```
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    numbers = [2, 3, 7, 9];
    print(remove_item(numbers, 3))  # [2, 7, 9]
    ```
11. 声明一个名为sum_all_numbers的函数。它接受一个number参数并将该范围内的所有数字相加。
```
print(sum_all_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
```
12. 声明一个名为*sum_of_odds*的函数。它接受一个数字参数，并将该范围内的所有奇数相加。
13. 声明一个名为*sum_of_even*的函数。它接受一个数字参数，并将该范围内的所有偶数相加。

### 练习2级
1. 声明一个名为*evens_and_odds*的函数。它取一个正整数作为参数，计算数字中偶数和奇数的个数。
    ```
    print(evens_and_odds(100))
    # 奇数的个数是 50.
    # 偶数的个数是 50.
    ```
2. 调用函数*factorial*，它接受一个整数作为参数并返回这个数的阶乘。
3. 调用自定义函数*is_empty*，它接受一个参数并检查它是否为空。

### 练习3级
1. 编写一个名为*is_prime*的函数，它检查一个数字是否是素数。
2. 编写一个函数来检查列表中是否所有项都是唯一的。
3. 编写一个函数来检查列表中的所有项是否都是相同的数据类型。

🎉 CONGRATULATIONS ! 🎉

[<< Day 10](../10_Day_Loops/10_loops.md) | [Day 12 >>](../12_Day_Modules/12_modules.md)
