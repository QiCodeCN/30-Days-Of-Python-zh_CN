
[<< Day 5](../05_Day_Lists/05_lists.md) | [Day 7 >>](../07_Day_Sets/07_sets.md)

- [Day 6:](#day-6)
  - [Tuple元组](#Tuple元组)
    - [创建元组](#创建元组)
    - [元组长度](#元组长度)
    - [元组取值](#元组取值)
    - [切片操作](#切片操作)
    - [转换tuple为list](#转换tuple为list)
    - [检查元组中项](#检查元组中项)
    - [元组的连接](#元组的连接)
    - [元组的删除](#元组的删除)
  - [💻 第6天练习](#-第6天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)

# Day 6

## Tuple元组

元组是不同数据类型的集合，它们是有序且不可变的。tuple 使用圆括号()包裹元素。它一旦被创建便不可修改。也就是说我们不能像上节学习的list一样更改集合项。同时也不能使用像 add，insert，remove等方法。在元组中仅有少量的方法，这些方法如下：

- `tuple()`：创建一个空的元组
- `count()`：计算元组中指定项的个数
- `index()`：返回指定项的索引值
- `+` ：连接两个或以上的元组成为新的元组

### 创建元组

元组的创建可以通过 `()` 或 `tuple()` 实现。在创建的时候也可以同时在括号内初始化数据项。
- 创建一个空的元组
  
```py
# 直接变量等于（）
empty_tuple = ()
# 或使用元组构造函数
empty_tuple = tuple()
```

- 元组创建并初始化数据
  
```py
# 语法
tpl = ('item1', 'item2','item3')
# 举例
fruits = ('banana', 'orange', 'mango', 'lemon')
```

### 元组长度

同之前学过的字符和列表一样，计算元组的长度使用 len() 内置函数。

```py
# # 语法形式
# tpl = ('item1', 'item2', 'item3')
# len(tpl)

# 实际举例
systems = ('Windowns','Linux','macOS')
print(len(systems)) # 3
```

### 元组取值

类似list数据类型，获取元组的项同样通过索引index方式。

- 正向索引：下角[0]表示元组项1，以此类推到元组长度减1

  ![Accessing tuple items](../images/day601_tuples_index.png)

  ```py
  # # 语法形式
  # tpl = ('item1', 'item2', 'item3')
  # first_item = tpl[0]
  # second_item = tpl[1]

  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[0]  # banana
  second_fruit = fruits[1] # orange

  last_index =len(fruits) - 1
  last_fruit = fruits[last_index]
  print(last_fruit) # lemon
  ```

- 负向索引：负索引表示从末尾开始，-1表示最后一项，-2表示第二项，元组长度的负数表示第一项。
  ![Tuple Negative indexing](../images/day602_tuple_negative_indexing.png)

  ```py
  # # 使用语法
  # tpl = ('item1', 'item2', 'item3','item4')
  # first_item = tpl[-4]
  # second_item = tpl[-3]

  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[-4]  # banana
  second_fruit = fruits[-3] # orange
  last_fruit = fruits[-1] # mango
  ```

### 切片操作

我们可以通过指定元组中起始和结束位置的索引范围来切出子元组，其中返回值将是一个包含指定项的新元组。

- 指定正向索引范围

  ```py
  # 语法形式
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # all items
  all_items = tpl[0:]         # all items
  middle_two_items = tpl[1:3]  # does not include item at index 3
  ```

  使用实战例子如下：_(其中请再次回忆第二行取所有元素右侧索引是4而不是3呢？)_
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # 所有元组项
  all_fruits= fruits[0:]      # 所有元组项
  orange_mango = fruits[1:3]  # 右3不包含index=3, print => ('orange', 'mango')
  orange_to_the_rest = fruits[1:] #print => ('orange', 'mango', 'lemon')
  ```

- 指定负向索引范围

  ```py
  # 语法形式
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # 所有项：从右侧倒数第四项，即正向index=0
  middle_two_items = tpl[-3:-1]  # 不包括索引3(-1)的项
  ```
  应用举例说明：
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # 所有项
  orange_mango = fruits[-3:-1]  # 不包括索引3的项，打印输出为 ('orange', 'mango')
  orange_to_the_rest = fruits[-3:] # 打印输出为 ('orange', 'mango', 'lemon')
  ```

### 转换tuple为list

我们可以在元组和列表之间相互转换。因为元组是不可变的，因此如果我们想改变它则需要转换成list。语法形式为list(元组)反之转换为tuple(列表)。以下看一些实际的例子：

```py
fruits = ('banana', 'orange', 'mango', 'lemon')

fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']

fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### 检查元组中项

我们可以使用`in`检查元组中是否存在指定项，它最终返回一个布尔值。

```py
# # Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# 'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

### 元组的连接

我们可以使用+操作符连接两个或多个元组。

```py
# # syntax
# tpl1 = ('item1', 'item2', 'item3')
# tpl2 = ('item4', 'item5','item6')
# tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

vegetables_and_fruits = vegetables + fruits
print(vegetables_and_fruits)
```

### 元组的删除

因为元组是不可变的。因此不能删除元组中的单个项，但可以使用del删除元组本身。

```py
# # 语法
# tpl1 = ('item1', 'item2', 'item3')
# del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits) # 提示错误 NameError: name 'fruits' is not defined

```


🌕 能走这么远，你真的很厉害。你已经完成学习挑战的第六天课程。今天内容虽然不多，但还是需要一些练习来检验下学习效果。

## 💻 第6天练习

### 练习1级

1. 用两种方式创建一个空元组
2. 创建两个具有关联的元组，如兄弟borthers 元组和 姐妹sisters 元组
3. 然后将其中一个分配另一个组成 兄弟姐妹siblings 元组
4. 请计算出新组合的元组（siblings）包含多少项
5. 通过类型转换方式，完成新项的添加，如爸爸和妈妈。最终形成 family_members 元组

### 练习2级

1. 从 family_members 拆分出 兄弟姐妹元组siblings 和 父母元组parents 
2. 首先创建 fruits, vegetables 和 animal 元组（记得每个初始化几个值）。然后将三个元组合并起来赋值给变量名为 food_stuff_tp 新元组。
3. 将元组 food_stuff_tp 转成列表 food_stuff_lt
4. 从 food_stuff_tp 元组 或 food_stuff_lt 列表中分隔出中间一项或者两项
5. 从 food_stuff_tp 分别分别获取到前三项和后三项
6. 彻底删除元组 food_staff_tp
7. 完成如下元素检查。原始元组为 nordic_countries:
  - 查看 'Estonia' 是否存在 nordic_countries 中
  - 查看 'Iceland' 是否存在 nordic_countries 中

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```

[<< Day 5](../05_Day_Lists/05_lists.md) | [Day 7 >>](../07_Day_Sets/07_sets.md)
