
[<< Day 8](../08_Day_Dictionaries/08_dictionaries.md) | [Day 10 >>](../10_Day_Loops/10_loops.md)

- [📘 Day 9](#-day-9)
  - [条件语句](#条件语句)
    - [如果if](#如果if)
    - [如果if 否则else](#如果if-否则else)
    - [if elif else](#if-elif-else)
    - [短条件语句](#短条件语句)
    - [嵌套条件语句](#嵌套条件语句)
    - [if 条件 and 逻辑运算符](#if-条件-and-逻辑运算符)
    - [if 条件 or 逻辑运算符](#if-条件-or-逻辑运算符)
  - [💻 第9天练习](#-第9天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)
    - [练习3级](#练习3级)

# 📘 Day 9

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## 条件语句
默认情况下，Python脚本中的语句从上到下依次执行。如果有逻辑处理需要，可以通过以下两种方式改变执行的顺序：

- 条件执行：如果某个表达式为真，则执行这个语句块；
- 重复执行：只要某个表式一直为真，则会重复执行一个语句或块。

在这节中，我们将学习到 if/else/elif 语句。因此前几节掌握的比较运算符和逻辑运算符在这里就会变得很有用。

### 如果if
在python和其他程序语言中，关键词 `if`用于检查条件是否真，并依此结果决定是否执行代码块。记住冒号后换行代码要缩进。

```python
# 语法形式
if condition:
    this part of code runs for truthy conditions
```

**演示例子：**
```python
a = 3
if a > 0:
    print('A 是正数')
# A 是正数
```

### 如果if 否则else
如果 `if` 条件是 `true` 那么第一个代码块将被执行，否则 else 条件将被运行。
```python
# 语法形式
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**演示例子：**
``` python
a = 3
if a < 0:
    print('A 是负数')
else:
    print('A 是正数')
```
上边的逻辑判断为假，因此else块被执行。但如果我们的田间超出两个呢？这时候就会用到 elif

### if elif else
在日常生活中，我们每天都要做决定。其中一些结果我们不能通过一两个条件得出，而是通过检查多个条件。编程和生活一样，也是充满条件的。当我们有多个条件时，我们使用 `elif`。
```python
# 语法形式
if condition:
    code
elif condition:
    code
else:
    code
```
**演示例子：**
```python
a = 0
if a > 0:
    print('A 是正数')
elif a < 0:
    print('A 是负数')
else:
    print('A 是零')
```

### 短条件语句
通常条件和语句块比较简单的时候，也可以使用短语句形式（类比其他语言中的三目运算符）。
```python
# 语法形式
code1 if condition else code2

# 实际举例
a = 3
print('A is positive') if a > 0 else print('A is negative') 
# 上边短条件语句满足第一个条件，“A是正的”将被打印
```

### 嵌套条件语句
条件语句是可以多层嵌套的
```python
# 语法形式
if condition:
    code
    if condition:
    code

# 具体举例
a = 0
if a > 0:
    if a % 2 == 0:
        print('A是一个正整数且是偶数')
    else:
        print('A是一个正整数)
elif a == 0:
    print('A是零')
else:
    print('A是负数')
```

但其实我们可以通过使用逻辑运算符，来避免过多的写嵌套条件代码。

### if 条件 and 逻辑运算符
``` python
# 语法形式
if condition and condition:
    code
```

*将上边嵌套代码改写举例：*
```python
a = 0
if a > 0 and a % 2 == 0:
        print('A是一个正整数且是偶数')
elif a > 0 and a % 2 !=  0:
     print('A是一个正整数')
elif a == 0:
    print('A是零')
else:
    print('A是负数')
```

### if 条件 or 逻辑运算符
```python
# 语法形式
if condition or condition:
    code
```

*演示举例：*
```python
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('权限通过!')
else:
    print('无权限!')
```

🌕 你做得很好。永远不要放弃，因为伟大的事情需要时间。你刚刚完成了第9天的挑战，你在通往伟大的道路上前进了9步。现在为你的大脑和肌肉做一些锻炼。

## 第9天练习
### 练习1级
1. 使用`input("输入你的年龄：")`获取用户输入。如果用户年龄在18岁以上，请给出反馈为：你的年龄可以学开车了。如果得到的年龄在18或以下，请给出还差几岁可以开车。 输出如：
    ```python
    输入你的年龄: 30
    你的年龄可以学开车了。

    输入你的年龄: 15
    你还需要 3 年才可以学开车。
    ```

2. 使用 `if...else` 比较 `my_age` 和 `your_age`。谁的年龄更大呢？同样使用input来获取你的年龄，其中我的年龄内置。你可以使用嵌嵌套条件打印 `year` 表示相差1岁，years表示相差更多，同时支持一个条件 my_age = your_age 即年龄相等。举例输出： 
    ``` python
    # 假设我的年龄是25
    请输入你的年龄: 30
    你比我大 5 years。 
    ```

3. 使用input获得两个数字。如果a比b大返回 a大于b，如果a比b小返回 a小于b，否则返回a与b相等。
    ```
    输入第一个数字: 4
    输入第二个数字: 3
    比较结果：4 大于 3
    ```

### 练习2级
1. 写一个段逻辑代码，并根据分数范围给出他们对应的等级。
    ```
    80-100, A
    70-89, B
    60-69, C
    50-59, D
    0-49, F
    ```

2. 检查季节是秋季、冬季、春季还是夏季。
- 如果用户输入为:September, October或November，则季节为Autumn；
- 如果输入是December、January或February，这个季节是Winter；
- March，April或May，季节则是Spring；
- June月，July或August，则季节是Summer。

3. 以下列举了一些水果:
    ```
    fruits = ['banana', 'orange', 'mango']
    ```
    然后获得输入的一种水果，如果列表中不存在，则将该水果添加到列表中并打印。如果已经存在则提示：该水果已经存在于列表中。

### 练习3级
1. 这里我们有一个人物字典。当然值你可以根据情况自己定义。
    ```python
     person={
        'name': 'MegaQi',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': ' 上海静安寺北京西路',
            'zipcode': '200041'
        }
    }
    ```
    然后分别分别实现下边条件判断要求：
    - 检查人员字典是否有 skill 键，如果有打印出对应的列表值。
    - 检查人员字典是否有 skill 键，如果有进一步检查这个人是否拥有Python技能，并打印出结果。
    - 如果这个人技能树仅是JavaScript和React，则打印”他是个前端开发人员“。如果技能树有Node、Python和MongoDB，则打印“他是个后端工程师”，如果这个人会Recat、Node和MongoDB，请打印“他是个全栈开发人员”，否则打印“未知标题” - 为了结果更准确可以使用嵌套条件语句。


🎉 CONGRATULATIONS ! 🎉

[<< Day 8](../08_Day_Dictionaries/08_dictionaries.md) | [Day 10 >>](../10_Day_Loops/10_loops.md)
