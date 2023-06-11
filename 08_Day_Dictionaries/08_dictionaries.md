
[<< Day 7 ](../07_Day_Sets/07_sets.md) | [Day 9 >>](../09_Day_Conditionals/09_conditionals.md)

- [📘 Day 8](#-day-8)
  - [Dict字典](#Dict字典)
    - [创建字典](#创建字典)
    - [字典长度](#字典长度)
    - [字典访问](#字典访问)
    - [字典增改](#字典增改)
    - [检查\复制\转换](#检查\复制\转换)
    - [移删清空](#移删清空)
    - [获取键或值列表](#获取键或值列表)
  - [💻 第8天练习](#-第8天练习)

# 📘 Day 8

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## Dict字典
字典是有序（在3.6+以后从无序变有序的）、可修改可变、成对(key:value)的数据类型集合。

### 创建字典
要创建一个dict类型，我们通过大括号`{}`或 内置函数方法 `dict()` 实现。
```
# 语法形式：空值
empty_dict = {}

# 语法形式：带初始值（键值对）
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```
实践例子
```python
person = {
    'name':'MegaQi',
    'age':100,
    'country':'China',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'Java', 'Python'],
    'address':{
        'city':'上海', 
        'street':'万航渡路'
    }
}
```
上面的例子中对应的值可以是任何数据类型，如：字符串、布尔值、列表、元组、集合或字典。
### 字典长度
使用`len(dict)`可以获得字典的长度，它计算的是一对 'key: value' 的数量。
```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```
具体例子
```python
person = {
    'name':'MegaQi',
    'age':100,
    'country':'China',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'Java', 'Python'],
    'address':{
        'city':'上海', 
        'street':'万航渡路'
    }
}
print(len(person)) # 6

```
### 字典访问
我们通过引用key的的方式获取dict键值对的值。形式为`字典变量[key]`
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
```
详细例子
```python
person = {
    'name':'MegaQi',
    'age':100,
    'country':'China',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'Java', 'Python'],
    'address':{
        'city':'上海', 
        'street':'万航渡路'
    }
}
print(person['name'])       # MegaQi
print(person['country'])    # China
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'Java', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # 万航渡路
print(person['school'])       # KeyError: school
```
如果访问key不存在则会引发错误。为了避免这种错误，首先必须检查键是否存在，或者可以使用`get`方法。如果键不存在，get方法会返回None，表示是一个NoneType对象数据类型。
```python
# 将上边的例子改成用get获取值
person = {
    #...略...
}
print(person.get('name')) 
print(person.get('country')) 
print(person.get('skills'))
print(person.get('city'))   # None
```
### 字典增改
#### 增加dict项
通过引用赋值，可以向已存在的字典中增加新的key-value项。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```
例子
```python
person = {
    # ...同上...
}
person['job_title'] = 'testcoder'
person['skills'].append('sql')
print(person)
```
#### 修改dict项值
同样的我们可以通过引用重新赋值一个项key对应值。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
```
尝试例子
```python
person = {
    # ...同上...
}
person['city'] = 'Beijing'
person['age'] = 150
print(person)
```
### 检查\复制\转换
#### 字典检查
要检查一个字典对是否存在，通过操作符`in`判断key是否在dict中包含。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# 例子
person = {
    # ...同上...
}
print('city' in person)  # True
print('school' in person) # Flase
```
#### 字典拷贝
使用`copy()`方法复制字典。使用复制可以避免原字典的项在操作中变动。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# 例子
person = {
    # ...同上...
}
copy_person = person.copy()
copy_person['city'] = '深圳'
print(person)
print(copy_person)
```
#### 字典转列表
方法`items()`将dictionary转换为元组列表。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```
### 移删清空
#### 字典项移除
移除字典中的项，可以通过以下三个方法：

- pop(key) ：移除具有指定键名的项，并返回移除项值
- popitem()：删除最后一项，并返回项值
- del：移除项通过关键名字
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # 移除key1项
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # 移除最后一项
del dct['key2'] # 移除第二项
```
例子
```python
person = {
    'name':'MegaQi',
    'age':100,
    'country':'China',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'Java', 'Python'],
    'address':{
        'city':'上海', 
        'street':'万航渡路'
    }
}
person.pop('name')         # 移除名字 name 第一项
person.popitem()           # 移除最后 address 项
del person['age']          # 移除 age 项
```
#### 清空字典项
如果不需要字典中的项，可以使用`clear()`方法清除它们。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# 实际例子
person = {
    # ...同上...
}
person.clear()
print(person) # {}
```
#### 删除整个字典
如果我们不使用字典，我们可以完全删除它。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# 实际例子
person = {
    # ...同上...
}
del person
print(person) # NameError: name 'person' is not defined
```
### 获取键或值列表
方法`keys()`可以获取字典中的所有键list。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```
方法`values()`可以获取字典中的所有值list。
```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```
🌕 你真非常厉害，你已经了解关于字典dict相关支持。你已经完成了第8天的挑战，现在让我们做一些练习巩固下吧。

## 💻第8天练习

1. 创建一个空的字典dict名字可以叫dog
2. 添加name, color, breed, legs, age 到 dog 字典
3. 创建一个 student 字典，并向其中添姓名name，年龄age，技能skills，国家country，城市city 和 地址项
4. 获取 student 字典的长度并打印
5. 获取项skills的值，并检查它的数据类型
6. 向skills中再添加1或两个技能
7. 获取一个字典的所有keys
8. 获取一个字典的所有values
9. 使用 `items()`方法将一个字典转成元组列表
10. 选择一个字典移除一项
11. 完整的删除掉一个字典dog或student

🎉 CONGRATULATIONS ! 🎉

[<< Day 7 ](../07_Day_Sets/07_sets.md) | [Day 9 >>](../09_Day_Conditionals/09_conditionals.md)
