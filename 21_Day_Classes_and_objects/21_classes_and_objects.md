
[<< Day 20](../20_Day_Python_package_manager/20_python_package_manager.md) | [Day 22 >>](../22_Day_Web_scraping/22_web_scraping.md)

- [📘 Day 21](#-day-21)
  - [类和对象](#类和对象)
    - [创建类](#创建类)
    - [创建对象](#创建对象)
    - [类构造函数](#类构造函数)
    - [对象方法](#对象方法)
    - [对象默认方法](#对象默认方法)
    - [用方法修改类的默认值](#用方法修改类的默认值)
    - [继承](#继承)
    - [重写父方法](#重写父方法)
  - [💻 第21天练习](#-第23天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)

# 📘 Day 21

## 类和对象
Python是一种面向对象的编程语言。Python中的所有东西都是一个对象，包括它的属性和方法。程序中使用的数字、字符串、列表、字典、元组、集合等都是相应内置类对象。我们创建类来创建对象。类，类似于对象构造函数，或者创建对象的“蓝图”。我们实例化一个类来创建一个对象。类定义对象的属性和行为，而另一方面，对象表示类。

从接受这个系列挑战开始，我们就在不知不觉中使用类和对象。Python程序中的每个元素都是类的对象。让我们检查一下python中的所有内容是否都是类：

```sh
> python
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### 创建类

要创建一个类，我们需要使用关键词 **class** 然后后边跟着名字和冒号，类的名字建议使用驼峰命名法。

```sh
# 语法形式
class ClassName:
  这里编写代码
```

**举例：**

```py
class Person:
  pass
print(Person)
```

```sh
<class '__main__.Person'>
```

### 创建对象

我们可以通过调用初始化类来创建对象。

```py
p = Person()
print(p)
# <__main__.Person object at 0x000002084C138490>
```

### 类构造函数

在上面的例子中，我们已经从Person类创建了一个对象。然而，没有构造函数的类，在实际应用程序中并没有真正的用处。让我们使用构造函数函数使我们的类更有用。与Java或JavaScript中的构造函数类似，Python也有内置的 `__init__()` 构造函数。**__init__** 构造函数带有self形参，它表示类的当前实例的引用。

**例子：**

```py
class Person:
      def __init__ (self, name):
          self.name =name

p = Person('MegaQi')
print(p.name)
print(p)
```
输出
```sh
MegaQi
<__main__.Person object at 0x000002DA62D18490>
```

让我们在构造函数中再添加一些参数

```py
class Person:
      def __init__(self, firstname, lastname, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.country = country
          self.city = city


p = Person('Mega', 'Qi', 'China', 'ShangHai')
print(p.firstname)
print(p.lastname)
print(p.country)
print(p.city)
```
输出
```sh
Mega
Qi
China
ShangHai
```

### 对象方法

对象可以有方法。方法属于对象的函数。

**举例:**

```py
class Person:
      def __init__(self, name, country, city):
          self.name = name
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.name} 居住在{self.country} {self.city}'

p = Person('Qi','中国', '上海')
print(p.person_info())
# Qi 居住在中国 上海
```

### 对象默认方法

有时候，你可能想为你的对象方法设置一个默认值。如果在构造函数中为形参指定默认值，就可以避免在不带形参的情况下调用或实例化类时出现错误。让我们看看它是什么样子的：
```py
class Person:
  def __init__(self, name='Qi', country='中国', city='上海'):
      self.name = name
      self.country = country
      self.city = city

  def person_info(self):
    return f'{self.name} 居住在{self.country} {self.city}'

p1 = Person()
print(p1.person_info())
p2 = Person('MeagaQi', '法国', '巴黎')
print(p2.person_info())
```
输出
```sh
# 默认给定参值
Qi 居住在中国 上海
# 指定参数值
MeagaQi 居住在法国 巴黎
```

### 用方法修改类的默认值

在下面的例子person类中，所有构造函数参数都有默认值。除此之外，我们还添加了一个技能参数，我们可以使用方法访问和修改它，比如向其中添加新的技能。

```py
class Person:
  def __init__(self, name='Qi',country='China'):
      self.name = name
      self.country = country
      self.skills = []
  
  def person_info(self):
      return f'{self.name} 住在 {self.country} 我的新技能树有 {self.skills}'
  
  def add_skill(self, skill):
      self.skills.append(skill)

class Student(Person):
  pass

s1 = Student('MegaQi', 'China')
s2 = Student('Tom', 'Finland')

print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

p = Person()
print(p.person_info())
p.add_skill('HTML')
p.add_skill('CSS')
p.add_skill('JavaScript')
print(p)
print(p.person_info())
print(p.skills)
```
输出
```sh
Qi 住在 China 我的新技能树有 []
<__main__.Person object at 0x0000023202118490>
Qi 住在 China 我的新技能树有 ['HTML', 'CSS', 'JavaScript']
['HTML', 'CSS', 'JavaScript']
```

### 继承

继承允许我们定义一个从父类继承所有方法和属性的类。父类或基类是提供所有方法和属性的类。子类是继承自另一个类或父类的类。

让我们通过继承 person 类来创建一个 student 类。

```py
class Student(Person):
    pass

s1 = Student('MegaQi', 'China')
s2 = Student('Tom', 'Finland')

print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```
输出
```sh
MegaQi 住在 China 我的新技能树有 []
['JavaScript', 'React', 'Python']
Tom 住在 Finland 我的新技能树有 []
['Organizing', 'Marketing', 'Digital Marketing']
```

我们没有在子类中调用 **__init__()** 构造函数。虽然我们不调用它，但我们仍然可以从父类访问所有属性。但是如果我们调用构造函数，我们可以通过调用 _super_ 来访问父属性。

我们可以给子类添加一个新方法，也可以通过在子类中创建相同的方法名来覆盖父类方法。比如当我们添加 **__init__**() 函数时，子类将不再继承父类的 **__init__**() 函数。

### 重写父方法

```py
class Person:
  def __init__(self, name='Qi',country='China'):
      self.name = name
      self.country = country
      self.skills = []
  
  def person_info(self):
      return f'{self.name} 住在 {self.country} 我的新技能树有 {self.skills}'
  
  def add_skill(self, skill):
      self.skills.append(skill)

class Student(Person):
    def __init__ (self, name='MegaQi', country='中国', gender="male"):
        self.gender = gender
        super().__init__(name, country)

    def person_info(self):
        gender = "他" if self.gender =='male' else '她'
        return f'{gender} 居住在 {self.country}。'

s1 = Student('ZhangSan', 'Finland','male')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

s2 = Student('Lidiya', 'England', 'female')
print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
他 居住在 Finland。
['JavaScript', 'React', 'Python']
她 居住在 England。
['Organizing', 'Marketing', 'Digital Marketing']
```

我们可以使用super()内置函数或父类名称Person自动从父类继承方法和属性。在上面的例子中，我们重写了父方法。子方法有一个不同的特点，它可以识别性别，根据输入的性别来决定使用哪个代词他或她。

🌕 现在，您已经完全拥有了编程的超级能力。现在来做些练习巩固下成果把。

## 💻 第21天练习

### 练习1级
1. Python有一个名为 _statistics_ 的模块，我们可以使用这个模块来进行统计计算。然而，为了学习如何制作函数和重用函数，让我们尝试开发一个程序，它可以计算样本的中趋势(均值，中位数，模态)和可变性(方差，标准偏差)的度量。除了这些测量之外，还要找到样本的最小值、最大值、计数、百分位数。您可以创建一个名为 **Statistics** 的类，并将所有执行统计计算函数创建为 Statistics 类的方法。

### 练习2级

1. 创建一个名为 _PersonAccount_ 的类，它有名字、收入、 花销属性，并且有类方法 total_income, total_expense, account_info, add_income, add_expense 和 account_balance。编写代码实现记账业务。



🎉 CONGRATULATIONS ! 🎉

[<< Day 20](../20_Day_Python_package_manager/20_python_package_manager.md) | [Day 22 >>](../22_Day_Web_scraping/22_web_scraping.md)
