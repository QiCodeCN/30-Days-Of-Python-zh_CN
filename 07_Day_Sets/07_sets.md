
[<< Day 6](../06_Day_Tuples/06_tuples.md) | [Day 8 >>](../08_Day_Dictionaries/08_dictionaries.md)

- [📘 Day 7](#-day-7)
  - [Sets](#sets)
    - [Creating a Set](#creating-a-set)
    - [Getting Set's Length](#getting-sets-length)
    - [Accessing Items in a Set](#accessing-items-in-a-set)
    - [Checking an Item](#checking-an-item)
    - [Adding Items to a Set](#adding-items-to-a-set)
    - [Removing Items from a Set](#removing-items-from-a-set)
    - [Clearing Items in a Set](#clearing-items-in-a-set)
    - [Deleting a Set](#deleting-a-set)
    - [Converting List to Set](#converting-list-to-set)
    - [Joining Sets](#joining-sets)
    - [Finding Intersection Items](#finding-intersection-items)
    - [Checking Subset and Super Set](#checking-subset-and-super-set)
    - [Checking the Difference Between Two Sets](#checking-the-difference-between-two-sets)
    - [Finding Symmetric Difference Between Two Sets](#finding-symmetric-difference-between-two-sets)
    - [Joining Sets](#joining-sets-1)
  - [💻 Exercises: Day 7](#-exercises-day-7)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 7

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## 集合Set

Set是项的合集。让我带你回到小学或者高中的数学课，集合的数学定义可以应用在python上。Set是无序且没有索引的集合。在Python中，集合用于存储唯一项，可以在集合之间查找并集、交集、差集、对称差集、子集、超集和不相交集。

> 百度百科概念：集合是指具有某种特定性质的具体的或抽象的对象汇总而成的集体。其中，构成集合的这些对象则称为该集合的元素。详细请搜索词条。

### 创建set

我们使用花括号 `{ }` 来创建一个set或 `set()` 内置函数。

- 创建一个空的 set

```py
# 语法1: 直接等于号
st = {}
# 或 初始化内置set函数
st = set()
```

- 创建一个带初始值的 set

```py
# 方法1：花括号内直接给项值
st = {'item1', 'item2', 'item3'}
# 例子1:
fruits = {'banana', 'orange', 'mango'}

# 方法2: set方法给定一个list作为初始值
st = set(['item1','item2'])
# 例子2:
fruits = set('banana','orange')
```

### 获取长度

我们使用 `len()` 方法来获取 Set 的长度。

```py
# 语法使用
st = {'item1', 'item2', 'item3'}
len(set)

# 实际列子
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

### 访问和检索

我们使用循环来访问项。具体将在循环部分看到如何使用。
而对于检查一项是否在set中我们使用操作符 `in`

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
# st中是否包含item3? 结果是 True
print("Does set st contain item3? ", 'item3' in st) 

# 具体例子
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### 项添加

Set一旦被创建，内部的项是不可以改变的。但是我们可以向其添加新项。

- 添加一个项使用 add()

```py
# 语法演示
st = {'item1', 'item2', 'item3'}
st.add('new_item')

# 具体例子
fruits = {'banana', 'orange', 'mango', 'lemon'} # len() 4
fruits.add('lime')
print(fruits) # len() 5
```

- 使用 update() 添加多个项，函数参数是一个list。

```py
# 语法：一次添加多个，最终st结果为item1～item7
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

# 具体例子
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)
print(len(fruits))
```

### 移删清空

### remove

我们可以使用 `remove()` 方法将set中某项进行移除。 其中如果移除的项不存在则会抛出一个错误，因此在做此操作前做好检查下项是否存在set中。不过我嗯可以使用 `discard()` 方法来进行同样操作但不会引起错误。

```py
# 语法
st = {'item1', 'item2', 'item3'}
st.remove('item2')

# 具体例子
fruits = {'banana', 'orange', 'mango'}
fruits.remove('orange') # 剩余 {'banana', 'mango'}
fruits.remove('lemon')  # 异常 Traceback (most recent call last):File "<stdin>", line 1, in <module> KeyError: 'lemon'

fruits.discard('lemon')  # 不会有任何异常提示
fruits.discard('banana') # 剩余 {'mango'}
```

还有一种 pop() 方法，它的作用是移除一个随机的项，并且返回移除项。

```py
# pop 举例
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
# 如果我们项得到随机移除项是什么直接赋值
removed_item = fruits.pop()
# 查看后两次pop剩余项 和 最后一次移除项值
print(fruits, removed_item)
```


#### clear

如果想清空或清除set集合，我们使用 `clear()` 方法。

```py
# 语法使用
st = {'item1', 'item2', 'item3'}
st.clear()

# 使用例子
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### del

如果我们想彻底删除set本身，我们使用 `del` 操作关键词。

```py
# 语法演示
st = {'item1', 'item2', 'item3'}
del st

# 举例
fruits = {'banana', 'orange', 'mango'}
del fruits
print(fruits) # NameError: name 'fruits' is not defined
```

### list转set

我们可以在list和set之间相互转换。将list转set的时候会移除重复项，仅有唯一值将被保留。

```py
# 语法
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
# 转后排序将是随机的，因为set是无序集合
st = set(lst)

# 具体例子
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
# 注意多试几次转换和打印看看每次转换后的排序输出
fruits = set(fruits) 
print(fruits) 
```

### 连接set

我们如果想将两个set组合在一起，可以使用union() 或 update() 方法。

- union 方法将两个set连接并返回一个新的set

```py
# 实战例子
fruits = {'banana', 'orange'} 
vegetables = {'tomato', 'potato', 'cabbage',}
print(fruits.union(vegetables)) # 注意无序这个关键点
```

- update 方法是将参数中set插入给定的set中

```py
# 实战例子
fruits = {'mango', 'lemon'}
vegetables = {'tomato', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'onion', 'tomato', 'carrot', 'mango'}
```

### 交集/差集

- 方法 `intersection()` 返回两个集合中的相同项的集合。

```py
# intersection 实战例子
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```

- 使用方法 `difference()` 它返回两个集合之间的差值。

```py
# difference 实战例子
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'t', 'y', 'p'} 结果是无序的输出和你的可能顺序不一致
dragon.difference(python)     # {'r', 'd', 'a', 'g'} 答案仅供参考，无序
```

### 检查子集/超集

集合可以是其他集合的子集或超集：
- 子集: `issubset()`
- 超集: `issuperset()`

```py
# 实战例子
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, 因为whole_numbers是个超集
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### 对称差集合

方法 `symmetric_difference()` 返回两个set之间的对称差。它意味着返回一个集合，其中包含两个集合中的所有项，然后除去两个都存在项，数学上对照：(A\B) ∪ (B\A)

```py
# 同样举个实际操作例子
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}
some_numbers.symmetric_difference(whole_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
# 再次强调set项无序，以下结果结果项相同
python.symmetric_difference(dragon)  # {'t', 'p', 'r', 'g', 'h', 'a', 'd', 'y'} 
dragon.symmetric_difference(python)  # {'t', 'p', 'r', 'g', 'h', 'a', 'y', 'd'}
```
> 这里请特别对照difference()弄清楚差和对称差的不同。


### 检查是否相同元素

如果两个集合没有一个或多个共同项，我们称它们为不相交集。我们可以使用 `isdisjoint()` 方法检查两个集合是连接的还是不连接的。或者可理解为用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。

```py
# 使用语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3','item5'}

st2.isdisjoint(st1) # False
st1.isdisjoint(st2) # False
```

实战操作例子

```py
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, 因为没有相同的项

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, 有相同的项 {'o', 'n'}
```

🌕 坚持到现在的你，就像一个冉冉升起的新星。你刚刚完成了第7天的挑战，你在通往伟大的道路上领先了7步。按照以往惯例，让我们来做一些练习，巩固下知识点。

## 💻 第7天练习

```py
# 已知有如下集合set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### 练习1级

1. 输出集合 it_companies 的长度
2. 添加 'Twitter' 到 it_companies
3. 一次添加多个公司到 it_companies
4. 从 it_companies 移除一家公司
5. 在移除set项操作中remove和difference方法有什么不同？

### 练习2级

1. 连接A和B
2. 找出 A intersection（交集） B 
3. 判断 A 是否是 B 子集
4. 判断 A 和 B 是否有相同元素（disjoint）
5. 实现 A join B 和 B join A
6. 在 A 和 B 的对称差
7. 完全的删除掉上边使用的过的集合

### 练习3级

1. 将年龄list转成set，并比较两者长度，哪个更大？
2. 解释以下数据类型的区别：字符串str、列表list、元组tuple和集合set
3. 有这样一个语句 " I am a teacher and I love to inspire and teach people "。 使用字符串split 和 set 得到唯一的单词集合。


🎉 CONGRATULATIONS ! 🎉

[<< Day 6](../06_Day_Tuples/06_tuples.md) | [Day 8 >>](../08_Day_Dictionaries/08_dictionaries.md)
