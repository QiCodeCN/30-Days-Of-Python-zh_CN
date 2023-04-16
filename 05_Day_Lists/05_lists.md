
[<< Day 4](../04_Day_Strings/04_strings.md) | [Day 6 >>](../06_Day_Tuples/06_tuples.md)

- [Day 5](#day-5)
  - [列表Lists](#列表Lists)
    - [如何创建list](#如何创建list)
    - [索引访问列表项](#索引访问列表项)
    - [负索引](#负索引)
    - [拆包列表项](#拆包列表项)
    - [切片操作列表](#切片操作列表)
    - [如何修改list](#如何修改list)
    - [检查list项](#检查list项)
    - [添加项到list](#添加项到list)
    - [插入项到list](#插入项到list)
    - [移除list项](#r移除list项)
    - [拷贝list](#拷贝list)
    - [连接list](#连接list)
    - [统计list项](#统计list项)
    - [查找项索引](#查找项索引)
    - [list项排序](#list项排序)
  - [💻 第5天练习](#-第5天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)

# Day 5

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## 列表Lists

在Python中有四种集合数据类型：
- 列表list：一个有序并且可修改的（可变）集合，允许有重复元素。
- 元组tuple：一个有序但不能改变或者修改的（不可变）集合，允许有重复元素。
- 集合set：一个无序，无索引且不可修改的集合。但可以向set中添加新的元素。不允许有重复元素。
- 字典dict：一个无序集合，可改变可修改，且有索引，没有重复元素。

本篇要学的 列表 是不同数据类型的集合，它们是有序和可修改的(可变的)。列表可以为空，也可以有不同的数据类型项。

### 如何创建list

Python中创建列表集有两种方式：

- 使用list内置函数

```py
# syntax
lst = list()
```

```py
# 使用方法,变量名lst并不是错别字，避免使用list=list()，因为list是python中关键字
lst = list() 

# 举例创建没有任何项的空list
empty_list = list()
print(len(empty_list)) # 0
print(empty_list)      # []
```

-  使用方括号 []

```py
# 使用方法
lst = []

# 声明一个空的list
empty_list = [] 
print(len(empty_list)) # 0
print(empty_list)      # []
```

如果一个列表带有初始值，我们可以使用 len() 方法计算列表的长度。

```py
# 定义一些列表变量并出示化一些相同类值
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']

# 打印列表长度
print('水果:', fruits)
print('水果数量:', len(fruits))
print('蔬菜:', vegetables)
print('蔬菜数量:', len(vegetables))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))

# 结果输出
水果: ['banana', 'orange', 'mango', 'lemon']
水果数量: 4
蔬菜: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
蔬菜数量: 5
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
```

列表中的元素可以包含数据类型

```sh
# 包含字符，数字，布尔，字典不同类型数据
lst = ['生活', 18, True, {'country':'中国', 'city':'ShangHai'}]
```

### 索引访问列表项

我们访问列表中的项使用索引，下角标从0开始。下图很清晰的展示索引所代表的项，最后一个为数组长度减1。

![List index](../images/day501_list_index.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
# 访问水果数组集的第一项
first_fruit = fruits[0]
print(first_fruit)      # banana

# 访问水果数组集的第二项
second_fruit = fruits[1]
print(second_fruit)     # orange

# 访问第最后一项：正向
last_fruit = fruits[3]
print(last_fruit) # lemon

last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

### 负索引

负索引表示从末尾开始，-1表示最后一项，-2表示倒数第二项。

![List negative indexing](../images/day502_ist_negative_indexing.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']

first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]

print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

### 拆包列表项

```py
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

具体举两个例子：

```py
# 第一个例子：水果拆分前三项给1，2，3变量，剩余全部给rest
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']

# 第二个例子：前三项和最后一项分别给了对应变量，剩余所有中间组成一个集合给到rest
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
```

### 切片操作列表

**正索引**：我们可以通过指定开始start、结束end指定索引范围，步指定间隔来返回一个新的列表。默认值start=0，end=len(列表) -1，step=1。

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits 返回所有水果
all_fruits = fruits[0:4] 
print(all_fruits) # ['banana', 'orange', 'mango', 'lemon']
 
# 此 all_fruits 和上边是同样的结果，切片end不设置表示到最后一个
all_fruits = fruits[0:]
print(all_fruits)  # ['banana', 'orange', 'mango', 'lemon']

# 它表示不包含index=0和index=3的项
orange_and_mango = fruits[1:3]
print(orange_and_mango) # ['orange', 'mango']

# 不包含banana
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon) # ['orange', 'mango', 'lemon']

# 这里演示了step第三个参数，表示每两个取一个，即隔一个项取值
banana_and_lemon = fruits[::2] 
print(banana_and_lemon)   # ['banana', 'mango']
```

**负索引**：同样我们可以通过负索引来对列表进行切片获取新的list操作。

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
# 返回水果的所有项
all_fruits = fruits[-4:]  # ['banana', 'orange', 'mango', 'lemon']

# 不包含首尾项，输出：['orange', 'mango']
orange_and_mango = fruits[-3:-1] 

# 从-3开始到结尾，输出：['orange', 'mango', 'lemon']
orange_mango_lemon = fruits[-3:]

# -1步将得到一个方向排序的list ['lemon', 'mango', 'orange', 'banana']
reverse_fruits = fruits[::-1]
```

### 如何修改list

List是可变（可修改）的有序项集合，修改的方法是通过列表索引重新赋值。

让我们修改水果列表为例：

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']

fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']

last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### 检查list项

判断某项是否存在list集合中使用 `in` 操作符。看如下例子：

```py
fruits = ['banana', 'orange', 'mango', 'lemon']

does_exist = 'banana' in fruits
print(does_exist)  # True

does_exist = 'lime' in fruits
print(does_exist)  # False
```

### 添加项到list

如果想要向已有的list中添加新的项，我们使用 `append()` 函数方法。请注意此方法是向末尾追加项。

```py
# syntax
lst = list()
lst.append(item)
```

```py
# 语法
# lst = list()
# lst.append(item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']

fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

### 插入项到list

上边append只能末尾追加新项，如果想在list某位置插入项，需要使用insert()方法。注意，此方法插入位置后边顺序往右移动。insert方法有两个参数：index索引 和 item插入项。

```py
# 语法形式
# lst = ['item1', 'item2']
# lst.insert(index, item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # 在orange和mango之间插入apple
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']

fruits.insert(3, 'lime')  # 新的list中在apple后插入新的职lime
print(fruits)   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
```

### 移除list项

#### Remove
使用 `remove()` 方法对list指定项进行移除。如果移除的项不存在则会报ValueError错误。

```py
# 语法形式
# lst = ['item1', 'item2']
# lst.remove(item)
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana') # 指定移除香蕉banana,如果有多个相同项，移除遇见的第一个
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']

fruits.remove('lemon') # 再移除lemon
print(fruits)  # ['orange', 'mango', 'banana']

fruits.remove('apple') # 移除不存在的项会报相应错误
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
```

#### Pop

方法函数 `pop()` 它删除指定的索引（如果没有指定index则删除最后一项）。

```py
# 语法形式
# lst = ['item1', 'item2']
# lst.pop()       # 默认最后一项
# lst.pop(index)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

这里请你尝试下如果如下两种情况会得到什么样结果：
- pop给定一个超出范围的index
- 对一个空列表[]使用pop

#### Del

此方法 `del()` 删除指定的索引。除此之外它还可以用于删除索引范围内的项，也可以完全删除列表。

```py
# 语法形式
# lst = ['item1', 'item2']
# lst_copy = lst.copy()

# 具体演示例子
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

fruits_copy[0] = 'apple'
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']
print(fruits)       # ['apple', 'orange', 'mango', 'lemon']
```

#### Clear

方法 `clear()` 可以清空整个 list:

```py
# 语法形式
lst = ['item1', 'item2']
lst.clear()
print(lst)  # []

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)  # []
```

### 拷贝list

通过 list2=list1 方法可以将一个list重新复制给一个新变量。这种方式下list2是list1的引用，任何在list2中的修改都将改变原是原始list1。但很多情况下，我们不希望改变原list，而是创建一个不关联的副本。避免上述问题的一种方式就是使用 `copy()` 方法函数。

```py
# 语法形式
# lst = ['item1', 'item2']
# lst_copy = lst.copy()

# 具体演示例子
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

fruits_copy[0] = 'apple'
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']
print(fruits)       # ['apple', 'orange', 'mango', 'lemon']
```

### 连接list

在Python中可以通过以下方式连接两个或多个列表。
- 方式一： 加号运算符（`+`），直接将两个list相加返回一个组合列表集合

```py
# 语法形式
# list3 = list1 + list2

# 具体演示例子
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers # 按相加顺序组合
print(integers) 
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) 
# # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- 方式二：使用 `extend()` 方法。此方法允许在原有list追加一个list。

```py
# 语法形式
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2)

# 具体演示例子
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) 
# Numbers: [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) 
# Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) 
# Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### 统计list项

方法 `count()` 返回一个项在列表中出现的次数。

```py
# 语法使用
# lst = ['item1', 'item2']
# lst.count(item)

# 实战演示例子
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### 查找项索引

方法 `index()` 返回给定项在list的索引。如果找不到返回ValueError：x is not in list。

```py
# 语法形式
# lst = ['item1', 'item2']
# lst.index(item)

# 案例
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, 第一次出现的位置
```

### list项排序

T要对列表进行排序，我们使用内置函数 sort() 或 sorted()。

- sort()：此排序方法将列表项按升序重新排序，并修改原始列表。如果方法参数reverse等于true，它将按降序排列列表项。

```py
# 语法使用
# lst = ['item1', 'item2']
# lst.sort()                # 默认升序
# lst.sort(reverse=True)    # 指定降序排序

# 例子
fruits = ['orange', 'banana', 'mango', 'lemon']
fruits.sort()
# 按字母排序，打印将输出 ['banana', 'lemon', 'mango', 'orange']
print(fruits) 

fruits.sort(reverse=True) # 字母降序
print(fruits) # ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort() # 数字小到大
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True) # 数字大到小
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
```

- sorted()：在于在不改变原是列表的情况下返回有序列表。注意使用语法是list作为一个参数传给sorted，而不是list的一个属性。
```py
# 直接举例
# 正序排序
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
print(fruits)           # ['banana', 'orange', 'mango', 'lemon']

# 倒叙排序
fruits = ['banana', 'orange', 'mango', 'lemon']
# 注意这里是倒序后重新赋值给了fruits，所以值顺序发生了变化
fruits = sorted(fruits,reverse=True) 
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
```

🌕 你非常勤奋，你并且取得了很大的成就。你当前完成了第5天学习，在完成挑战的路上迈出了5步。现在让我们通过练习好好回忆和巩固下在list所学的知识吧。 

## 💻 第5天练习

### 练习1级

1. 声明一个空的 list。
2. 声明一个list并初始化5项数据。
3. 计算刚刚声明list的长度。
4. 分别获取第一、中间和最后一个列表项。
5. 声明一个名为mixed_data_types的list，然后赋予以下不同类型数据：你的姓名，年龄，是否毕业，身高，家庭地址。
6. 声明list变量名为 it_companies 并且初始化一些公司数据 Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon。
7. 使用 print() 打印刚刚声明的 it_companies。
8. 计算打印公司list的项的个数。
9. 分别输出第一、中间和最后公司名。
10. 任意更改公司list中一数据，然后打印出来。
11. 追加一个新公司到 it_companies。
12. 再新增公司到list中间的位置。
13. 选择 it_companies 一项非全大写名更改其全部大写。
14. 使用引号内字符'#;' 将 it_companies 列表数据连接起来。
15. 搜索一个公司是否存在it_companies 列表内。
16. 使用方法 sort() 对其list进行排序。
17. 使用 reverse() 降序排序。
18. 切片方式获取it_companies的前三项。
19. 切片方式获取it_companies的后三项。
20. 切片方式获取位于列表中间的几项。
21. 从列表中移除第一个公司。
22. 从列表中移除中间的一家公司。
23. 从列表中移除最右一家公司。
24. 从列表中移除所有公司。
25. 删除/销毁 it_companies 列表。
26. 将下边给出的list进行合并连接。

```py
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
```

27. 在完成26题后，拷贝copy这个列表到一新列表变量full_stack。然后在Redux后插入Python和SQL。


### 练习2级

1. 有如下一个包含10名同学年龄的list，根据要求完成练习。

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- 通过排序然后找出最小和最大年龄；
- 添加一个更小和更大的年年龄数到ages列表中；
- 找出中位数年龄(中间一项或中间两项除以二)；
- 找出平均年龄(所有项目的总和除以它们的数量)；
- 找出年龄的范围(最大值-最小值)。
- 比较(min - average)和(max - average)的值，使用abs()方法。

2. 有列表如：['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']，现将前三个国家和其他国家拆开。

🎉 CONGRATULATIONS ! 🎉

[<< Day 4](../04_Day_Strings/04_strings.md) | [Day 6 >>](../06_Day_Tuples/06_tuples.md)
