
[<< Day 9](../09_Day_Conditionals/09_conditionals.md) | [Day 11 >>](../11_Day_Functions/11_functions.md)


- [📘 Day 10](#-day-10)
  - [循环](#循环)
    - [while](#while)
    - [while break](#while-break)
    - [while continue](#while-continue)
    - [for](#for)
    - [for break](#for-break)
    - [for continue](#for-continue)
    - [范围函数 range](#范围函数-range)
    - [嵌套循环](#嵌套循环)
    - [for else](#for-else)
    - [pass](#pass)
  - [💻 第10天练习](#-第10天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)

# 📘 Day 10

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## 循环
生活中充满了例行公事。在程序中一样，也要做很多重复的工作。编程语言使用循环处理这些重复任务。Python编程语言提供以下两种循环：
- while 循环
- for 循环

### while
我们使用保留字 `while` 进行一种循环。在符合给定的条件之内，它会一直重复执行语句块。当条件为`false`时，代码将跳出循环。
```
# 语法形式
while condition:
    code goes here
```
举例
``` python
count = 0
while count < 5:
    print(count)
    count = count + 1
# 将打印 0 到 4
```

在上边的while循环中，当count加到5的时候条件变成了false，这时循环停止了。如果想条件不满足的时候执行其他代码块，我们可以使用 `else`。
```
# 语法
while condition:
    code goes here
else:
    code goes here
```
举例
```js
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```
当count=5的时条件变为false，循环停止并执行else下语句块。结果最后值5被打印出来。

### while break
当我们想要跳出或停止循环时，我们使用`break`。
```
# 语法
while condition:
    code goes here
    if another_condition:
        break
```
实际举例
```python
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```
上面的while循环只打印0、1、2，但是当它到达3时就停止了。

### while continue
通过`continue`语句，我们可以跳过当前迭代，并继续下一个迭代。
```
# 语法
while condition:
    code goes here
    if another_condition:
        continue
```
举例
```python
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
```
以上while循环仅打印0，1，2 和 4（其中3被忽略）。

### for
另一种循环方式是使用关键词 `for` 。类似其他语言的for循环，但又有一些差异点。Python中迭代序列可以是 list、tuple、dict、set 或 str。

- list 列表 for 迭代
``` python
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number是引用列表项的临时名称，仅在此循环内有效
    print(number)       # 数字将从0到5逐行打印
```

- str 字符 for 迭代
```python
# 拆分python字符串
language = 'Python'
for letter in language:
    print(letter)

# 通过下脚标访问打印
for i in range(len(language)):
    print(language[i])

# 以上两个输出均为
P
y
t
h
o
n
```

- tuple 元组 for 迭代
``` python
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# 依次换行打印 0-5
```

- dict 字典 for 迭代
  1. 默认循环字典时候会迭代字典的key
    ```python
    person = {
        'name':'MegaQi',
        'age':180,
        'country':'China',
        'is_marred':True,
        'skills':['Java', 'React', 'Node', 'Mysql', 'Python']
    }

    for key in person:
        print(key)
    ```
  2. 可以同时循环取得key和value
    ```python
    person = {
        'name':'MegaQi',
        'skills':['Java', 'React', 'Node', 'Mysql', 'Python'],
        'address':{
            'city':'上海',
            'code':'021'
        }
    }

    for key, value in person.items():
        print(key, value)
    ```

- set 集合 for 迭代
```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```
### for break
同while break相同，如果想停止迭代使用关键词 `break`。
```
# 语法形式
for iterator in sequence:
    code goes here
    if condition:
        break
```
举例
```
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```
在上面的例子中，循环在达到3时执行break停止继续迭代。

### for continue
同理也可以使用`continue`忽略本迭代后边操作。
```
# 语法
for iterator in sequence:
    code goes here
    if condition:
        continue
```
举例
```python
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('下一个数字将是 ', number + 1) if number != 5 else print("循环结束") # 注意此处使用短条件语句
print('循环外部')
```
在上面的例子中，如果数字等于3，则跳过条件之后的步骤(在循环内部)，如果还未完成迭代，则继续执行循环。

### 范围函数 range
函数 `range()` 按给参数值返回一个数字列表。函数 `range(start, end, step)` 有三个参数：开始、结束和增数。默认情况下，它从0开始，增量为1。范围序列至少需要一个参数(end)。它将创建一个范围序列。
```python
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 给了两个参数表示开始到结束，默认增长值1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```
注意range第一个参数start是包含本身，而第二个参数end是不包含本身。

它可以直接应用在for循环上
``` 
# 使用形式
for iterator in range(start, end, step):
```
举例
```python
for number in range(11):
    print(number)   # 打印0-10（不包含11）
```

### 嵌套循环
我们可以使用多层循环。语法形式如下：
```
for x in y:
    for t in x:
        print(t)
```
实操例子
```python
person = {
    'name': 'MegaQi',
    'country': 'China',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'city': 'ShangHai',
        'code': '021'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```
以上字典中技能是个列表，那增加一个条件判断，当关键词等于skills时，增加一个循环打印技能列表。

这里大家可以扩展两点思考：
- 下如果再增加一个判断循环打印地址内对应的key和value又如何操作呢？
- 我们能否for 和 while混用呢？如果可以将如何改写。

### for else
如果我们想在循环结束时执行逻辑外代码则使用else。
```
# 语法形式
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```
实际举例
```python
for number in range(11):
    print(number)   # 打印 0 到 10
else:
    print('迭代停止于：', number)
```

### pass
在python中，语法冒号后必须要给定执行语句。但有时候我们不希望做任何事情。为了避免语法的错误，使用`pass`关键词做占位符。
```python
# 输出了寂寞
for number in range(6):
    pass

# 跳过4
for number in range(6):
    if number == 4:
        pass
    else:
        print(number)
```

🌕你实现了一个巨大的里程碑，你是不可阻挡的。继续前进!你 刚刚完成了第10天的挑战，你向你的伟大之路前进了10步。现在趁热打铁块来巩固下，做些适应性练习吧。

## 第10天练习
### 练习1级
1. 使用for循环打印0-10，然后用while实现同样功能
2. 使用for循环打印10-0，然后同样用while实现
3. 编写一个打印循环（7次），输出如下的三角图案:
    ```
    #
    ##
    ###
    ####
    #####
    ######
    #######
    ```
4. 使用嵌套循环创建如下输出
    ```
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    ```
5. 利用循环方法打印以下图案:
    ```
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100
    ```
6. 使用for循环遍历列表['Python'， 'Numpy'，'Pandas'，'Django'， 'Flask']，并打印其项
7. 使用for循环0到100，且只打印偶数
8. 使用for循环0到100，但只打印奇数

### 练习2级
1. 使用for循环从0到100进行迭代，并输出所有数字的和。
    ```
    所有数据相加总和 = 5050
    ```
2. 使用for循环从0到100进行迭代，并输出所有偶数和所有奇数的和。
    ```
    所有偶数的和是2550。所有奇数的总和是2500。
    ```

🎉 CONGRATULATIONS ! 🎉

[<< Day 9](../09_Day_Conditionals/09_conditionals.md) | [Day 11 >>](../11_Day_Functions/11_functions.md)
