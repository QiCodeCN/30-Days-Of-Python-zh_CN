
[<< Day 17](../17_Day_Exception_handling/17_exception_handling.md) | [Day 19>>](../19_Day_File_handling/19_file_handling.md)

- [📘 Day 18](#-day-18)
  - [正则表达式](#正则表达式)
    - [*re* 模块](#re-模块)
    - [*re* 函数](#re-函数)
      - [match](#match)
      - [search](#search)
      - [findall](#findall)
      - [sub](#sub)
      - [split](#split)
  - [正则语法](#正则语法)
    - [方括号 []](#方括号-[])
    - [转义 \\](#转义-\\)
    - [一或多次 +](#一或多次-+)
    - [任意字符 .](#任意字符-.)
    - [零或多次 *](#零或多次-*)
    - [零或一次 ?)](#零或一次-?)
    - [数量 {}](#数量-{})
    - [开头 ^](#开头-^)
    - [不包含 [^]](不包含-[^])
  - [💻 第18天练习](#-第18天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)
    - [练习3级](#练习3级)

# 📘 Day 18

> 🎉 本系列为Python基础学习，原稿来源于 [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) 英文项目，大奇主要是对其本地化翻译、逐条验证和补充，想通过30天完成正儿八经的系统化实践。此系列适合零基础同学，或仅了解Python一点知识，但又没有系统学习的使用者。总之如果你想提升自己的Python技能，欢迎加入《挑战30天学完Python》

## 正则表达式

正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。要在python中使用RegEx，首先我们应该导入名为 *re* 的模块。

### *re* 模块

导入模块以后，我们就可以使用它来检查或者查找了。

```py
import re
```

### *re* 函数

为了使用不同的模式进行查找， *re* 提供了一些函数方法来进行匹配。

* *re.match*: 只在字符串的第一行开始搜索，如果找到则返回匹配的对象，否则返回None。
* *re.search*: 如果字符串(包括多行字符串)中有匹配对象，则返回匹配对象。
* *re.findall*: 返回包含所有匹配项的列表，如果没有匹配则返回空列表。
* *re.split*:	方法按照能够匹配的子串将字符串分割后返回列表。
* *re.sub*:  查找并替换一个或者多个匹配项。

#### Match

```py
# 语法形式
match(pattern, string, flags=0)
# pattern： 匹配的正则表达式
# string：要匹配的字符串
# flags：[可选] 用来控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
```

```py
import re

txt = 'I love to teach python and javaScript'
# 本身反馈一个 span 对象
match = re.match('I love to teach', txt, re.I)  # re.I 不区分大小写
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# 进一步我们可以使用span()获取匹配的起始位置和结束位置的元组值
span = match.span()
print(span)     # (0, 15)

# 再进一步可以打印出拆分的起始和结束索引，以及使用分片获取匹配字符串
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```

如例上边例子中示，我们在目标字符串中查找是否有 *I love to teach* 的字符串匹配。其中从开始的位置我们找到了对应匹配，进而得到了一个对象的返回。

```py
import re

txt = 'I love to teach python and javaScript'
match1 = re.match('I like to teach', txt, re.I)
print(match1)  # None

match2 = re.match('love', txt)
print(match2)  # None

```

此例子中字符串不包含 *I like to teach*，或者没用匹配开头字符，因此匹配方法返回None。

#### Search

```py
# 语法
re.search(pattern, string, flags=0)
# 参数说明同match
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# 返回匹配对象span
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

# 获取匹配开始和结束位置元组
span = match.span()
print(span)     # (100, 105)

# 获取开始和结束值，并获截取字字符串
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

# 没有任何匹配返回None
nom = re.search('weather', txt, re.I)
print(nom)  # None

```

正如你所见，搜索要比匹配方式好的多。因为它可以在整个文本中进行查找匹配。并返回第一找到的对象，否则返回None。接下来还有一个更好的函数 *findall* 它可以匹配所有并以列表形式返回。

#### findall

*findall()* 以列表的形式返回所有匹配

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

可以看到，单词 *language* 在字符串中出现了两次。现在我们将在字符串中寻找Python和Python单词:


```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

这个例子中因为我们使用标记位（re.I) 忽略大小写，所以返回两个。如果我们没有使用它，看看是什么结果。

```py
import re
matches = re.findall('Python', txt)
print(matches)  # ['Python']

```
当然我们如果想要达到其他效果，也可以用其他方法，不过就没有上边使用标记位那么优雅了。

```py
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

#### sub

匹配并替换字符串，直接看例子：

```py
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

# 或者
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
```

让我们再来看一个例子。下边是一个包含很多多余 % 字符的字符串，让人晦涩难懂。让我们用此方法清楚掉它。

```py
import re
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```
得到整洁的文本输出
```sh
I am teacher and  I love teaching. 
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?
```

#### split

返回分割后的列表。

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # 按照换行符 \n 进行分割返回

# 其实等同于字符直接调用split方法
print(txt.split('\n'))  
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## 正则语法

在以往我们声明一个变量，使用的是单引号或者双引号。如果要声明一个正则变量则是 `r''`
下面的模式仅用小写字母标识apple，为了使其不区分大小写，我们要么重写模式，要么添加一个标志。

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# 添加标记位使其大小写不敏感
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']

# 或者我们使用一组规则匹配方法
regex_pattern = r'[Aa]pple'  # [Aa]表示匹配字符串首字符可以是大写A，也可以是小写a
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```
这里先附上标记位包含哪些：
* re.I：匹配对大小写不敏感
* re.M：多行匹配（影响 ^ 和 $）
* re.S：使 . 匹配包括换行在内的所有字符

然后就详细看下正则里的一些语法符
* []:  一组字符
  * [a-c] 表示 a 或 b 或 c
  * [a-z] 表示 小写 a 到 z 任意字符
  * [A-Z] 表示 大写 A to Z 任意字符
  * [0-3] 表示 0 或 1 或 2 或 3
  * [0-9] 表示0 到 9 任意数字
  * [A-Za-z0-9] 表示任意单字符, 即 小写字母a到z, 大写字母A到Z 或数字0到9
* \\:  转义特殊字符
  * \d 表示 匹配任意数字，相当于 [0-9].
  * \D 表示 匹配任意非数字
* . : 匹配任意字符（除了换行符 \n）
* ^: 匹配开头
  * r'^substring' 例如 r'^love', 必须以love开头的句子
  * r'[^] 表示不在[]中的字符，例如 r'[^abc] 表示不是a, 不是b, 不是c。即除a,b,c之外的字符
* $: 匹配结尾
  * r'substring$' 举例 r'love$', 必须以love结尾的句子
* *: 0或多个次
  * r'[a]*' 表示可以不出现，或者可以出现多次
* +: 0或多个次
  * r'[a]+' 表示至少一次或多次
* ?: 0或1次
  *  r'[a]?' 表示零次或一次
* {n}：精确匹配个数
  * {3}: 表示 正好3个字符
  * {3,}: 表示 至少3个字符
  * {3,8}: 表示 3到8个字符
* |: 不是就是（或）
  * r'apple|banana' 表示要么是 apple 要么是 banana
* (): 正则表达式分组并记住匹配的文本

![Regular Expression cheat sheet](../images/day1801_regex.png)

让我们用一些例子来上边这些匹配字符是如何使用的。

### 方括号 []

让我们用方括号来匹配小写和大写

```py
import re

regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

如我我们想再额外查找 banana，我们可以优化匹配如下：

```py
import re

regex_pattern = r'[Aa]pple|[Bb]anana' 
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

我们在方括号中使用了字符或 *|* ，因此设法提取出了 Apple, Apple, Banana 和 Banana。

### 转义 \\

```py
import re

regex_pattern = r'\d'  # 
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], 提取了所有数字，但这却不是我们想要的效果
```

### 一或多次 +

结合上边 *\d* 使用+做个组合优化 
```py
import re

regex_pattern = r'\d+'  # d表示匹配数字, +表示一次或多次
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - 现在才是我们想要的效果
```

### 任意字符 .

```py
import re

regex_pattern = r'[a].'  # 小写a和任意
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)  # 匹配多个项目
print(matches)  # ['an', 'an', 'an', 'a ', 'ar'] 分别对应and中an，banana中an、an、a空格，are中ar 

regex_pattern = r'[a].+'  # . 任意字符, + 一次或多次（连续）
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### 零或多次 *

零次或多次。即可能不会出现，也可能多次出现。

```py
import re

regex_pattern = r'[a].*'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### 零或一次 ?

零次或一次。即可能不会出现，也可能只出现一次。

```py
import re

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? 表示 - 是个可选项
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### 正则数量 {}

我们可以使用花括号指定我们在文本中寻找的子字符串的长度。让我们想一下，我们如果对一个长度为4个字符的子字符串感兴趣的话：

```py
import re

txt = '今年的大年三十日期是2023年1月23日，去年的则是2022年1月31日，真是一年比一年早'
regex_pattern = r'\d{4}'  # 精准匹配有四个数字的
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2023', '2022']

regex_pattern = r'\d{1,4}'   # 匹配1,2,3,4 贪婪模式
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2023', '1', '23', '2022', '1', '31']
```

### 开头 ^

* 匹配字符串的开头
  
```py
import re

txt = '今天天气很好，所以今天你的心情好吗？'
regex_pattern = r'^今天'  # ^ 表示必须以“今天”开头
matches = re.findall(regex_pattern, txt)
print(matches)  # ['今天'] 注意只返回了一个
```

### 不包含 [^]

```py
import re

txt = '今年的大年三十日期是2023年1月23日，去年的则是2022年1月31日，真是一年比一年早'
regex_pattern = r'[^\u4e00-\u9fa5， ]+'  # ^ 排除中文字符，逗号和空格
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2023', '1', '23', '2022', '1', '31']
```

## 💻 第18天练习

### 练习1级
 1. 下面这段话中出现频率最高的单词是什么?
```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```sh
    [
      (6, 'love'),
      (5, 'you'),
      (3, 'can'),
      (2, 'what'),
      (2, 'teaching'),
      (2, 'not'),
      (2, 'else'),
      (2, 'do'),
      (2, 'I'),
      (1, 'which'),
      (1, 'to'),
      (1, 'the'),
      (1, 'something'),
      (1, 'if'),
      (1, 'give'),
      (1, 'develop'),
      (1, 'capabilities'),
      (1, 'application'),
      (1, 'an'),
      (1, 'all'),
      (1, 'Python'),
      (1, 'If')
    ]
```

2. 从以下这段对话中提取数字 "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction." 并计算出最远距离点。

```py
points= ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points= [-12, -4, -3, -1, 0, 4, 8]
distance = |-12| + |8|  # 20
```

### 练习2级

1. 编写一个方法来识别字符串是否是有效的python变量
    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```

### 练习3级
1. 清除以下文本无用的字符。且统计出优化后的文本中出现频率最高的三个单词。

    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence))
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```

🎉 CONGRATULATIONS ! 🎉

[<< Day 17](../17_Day_Exception_handling/17_exception_handling.md) | [Day 19>>](../19_Day_File_handling/19_file_handling.md)