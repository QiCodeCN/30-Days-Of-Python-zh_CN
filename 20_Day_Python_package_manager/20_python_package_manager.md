
[<< Day 19](../19_Day_File_handling/19_file_handling.md) | [Day 21 >>](../21_Day_Classes_and_objects/21_classes_and_objects.md)

- [📘 Day 20](#-day-20)
  - [Python PIP 包管理](#Python-PIP-包管理)
    - [什么是 PIP ?](#什么是-PIP)
    - [安装 PIP](#安装-PIP)
    - [使用pip安装包](#使用pip安装包)
    - [卸载包](#卸载包)
    - [查看包列表](#查看包列表)
    - [查看包信息](#查看包信息)
    - [PIP Freeze](#pip-freeze)
    - [从WEB中读取数据](#从WEB中读取数据)
    - [创建包](#创建包)
    - [关于更多包的信息](#关于更多包的信息)

# 📘 Day 20

## Python PIP 包管理

### 什么是 PIP ?

PIP是Python第三方库管理器，我们可以通过 _pip_ 来安装不同的Python包。
包是一个Python模块，可以包含一个或多个模块或其他包。即可以安装到应用程序中的一个或多个模块就是一个包。
在实际的编程中，我们不必去编写每一个实用程序，很多有别人已经封装好的，我们可以导入到程序中直接使用。

### 安装 PIP

如果你是通过程序安装的python环境，那么默认pip已经在其中了，让我们打开终端查看：

```sh
>pip --version
pip 21.1.1 from c:\programdata\python38\lib\site-packages\pip (python 3.8)
```

如你所见, 我当前使用的 pip 版本是 21.1.1。如果你到其他版本数字都证明，pip已经被安装，可以正常使用。

让我们检查一下Python社区中用于不同编码的一些包。注意，这些演示只是想让你知道有很多包可以用于不同的应用程序，并不展开讲解。

### 使用pip安装包

让我们首先来安装一个叫 _numpy_ 的包。它是机器学习和数据科学社区中最受欢迎的软件包之一。

NumPy是使用Python进行科学计算的基本包。它还包括:
- 一个强大的n维数组对象
- 复杂的(广播)功能
- 集成C/ c++和Fortran代码的工具
- 有用的线性代数\随机数等功能

```sh
> pip install numpy
Successfully installed numpy-1.24.2
```

当你看到提示successfully的字样表示安装成功，事实上可能你本地已经有了此包，你可以通过 `pip uninstall numpy` 先卸载，然后再体验安装过程。

包numpy安装成功后，让我们看下如何使用：

```sh
> python
Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.24.2'
>>> list = [1,2,3,4,5]
>>> np_arr = numpy.array(list)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr + 2
array([3, 4, 5, 6, 7])
>>>
```

Pandas是一个BSD许可开放源码库，为Python编程语言提供高性能、易于使用的数据结构和数据分析工具。让我们安装比numpy更高级的 _pandas_ ：

```sh
> pip install pandas
```
终端上练习导入和使用
```py
> python

>>> import pandas as pd
>>> df = pd.Series(0, index=['1', '2', '3', '4'])
>>> print(df)
1    0
2    0
3    0
4    0
dtype: int64
```

本节不细化关于numpy或pandas内置函数功能，在这里我们仅尝试学习如何安装软件包以及如何导入它们。如果需要，我们将在其他部分讨论不同的包。

接下来，让我们导入一个网页浏览器模块，它可以帮助我们打开任何网站。我们不需要安装这个模块，因为它已经在Python 3中默认安装了。例如，如果你想在任何时间打开任意数量的网站，或者如果你想安排一些事情，你可以利用 _webbrowser_ 模块。

```py
import webbrowser 

# url列表
url_lists = [
    'http://www.python.org',
    'https://github.com/QiCodeCN'
]

# 浏览器通过标签页打开
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### 卸载包

如果您希望不再保留已安装的包，您可以使用以下命令删除它们。

```sh
pip uninstall packagename
```

### 查看包列表

查看我们机器上已安装的包。我们可以用 pip list 命令。

```sh
pip list

Package               Version
--------------------- -----------
anyascii              0.3.1
appdirs               1.4.4
... 省略 ...
```

### 查看包信息

查看包的详细信息，可以使用show + 包名

```sh
pip show packagename
```
比如查看上边安装好的pandas包详细
```sh
>pip show pandas
Name: pandas
Version: 1.5.2
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
Author-email: pandas-dev@python.org
License: BSD-3-Clause
Location: c:\programdata\python38\lib\site-packages
Requires: python-dateutil, numpy, pytz
Required-by: TTS
```

上边是列了基本的信息，如果你想看更多信息，请加上参数 --verbose

```sh
>pip show --verbose pandas
Name: pandas
Version: 1.5.2
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
Author-email: pandas-dev@python.org
License: BSD-3-Clause
Location: c:\programdata\python38\lib\site-packages
Requires: pytz, python-dateutil, numpy
Required-by: TTS
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Intended Audience :: Science/Research
  License :: OSI Approved :: BSD License
  Operating System :: OS Independent
  Programming Language :: Cython
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3 :: Only
  Programming Language :: Python :: 3.8
  Programming Language :: Python :: 3.9
  Programming Language :: Python :: 3.10
  Programming Language :: Python :: 3.11
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

当我们代码稳定稳定后，通常代码迁移时候，需要获取Python项目依赖包的安装列表，以便别人能够快速安装。这个列表要包括需要安装什么包、以及包的版本。通常我们输出到 requirements.txt 文件中。

```sh
> pip freeze > requirements.txt
```
注意：freeze默认是python环境所有包，如果想仅保持单独项目的，尽量使用虚拟环境。下边命令演示了如何根据requirements一键安装。

```sh
> pip install -r requirements.txt
```


### 从WEB中读取数据

到目前为止，您已经熟悉了如何读取或写入本地计算机上的文件。但有时，我们想从一个网站读取信息，比如从url或API。

API是应用程序接口的缩写。它是一种在服务器之间交换结构化数据的方法，主要是为json数据。要打开一个网络连接，我们需要一个名为 _requests_ 的包——它允许打开一个网络连接并实现CRUD（创建、读取、更新和删除）操作。在本节中，我们将只讨论CRUD的读取和获取部分。

同样首先安装 _requests_ 模块包:

```py
> pip install requests
```

我们可以了解它的 _get_, _status_code_, _headers_, _text_ 和 _json_ 方法：
  - _get()_：打开一个网络并从url中获取数据-它返回一个响应对象
  - _status_code_：在我们获取数据后，我们可以检查操作的状态(成功，错误等)
  - _headers_：检查头信息类型
  - _text_：从获取的响应对象中提取文本
  - _json_：提取json数据

让我们读取一个txt文件从这个网址中 https://www.w3.org/TR/WD-html40-970708/html40.txt

```py
import requests # 导入模块

url = 'https://www.w3.org/TR/WD-html40-970708/html40.txt' # 定义要读取的地址变量

response = requests.get(url) # 请求地址并获取返回数据
print(response)
print(response.status_code) # 打印状态, success:200
print(response.headers)     # 头信息
print(response.text) # 查看所返回的数据文本 注意如果地址无法访问时候内容是404
```

- 让我们从API中读取。API是应用程序接口的缩写。它是一种在服务器之间交换结构数据的方法，主要是json数据。

```py
import requests
url = 'https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city='  # 国内可访问天气接口
response = requests.get(url) 
print(response) 
print(response.status_code) 
weather = response.json() 
print(weather)
```

两个请求中最后一个直接可以获取json对象。但如果不是JSON数据类型返回，我们通常都使用text获取，然后再根据需要进行转换或者处理。

### 创建包

我们根据一些标准将大量的文件组织在不同的文件夹和子文件夹中，这样我们就可以很容易地找到和管理它们。如你所知，一个模块可以包含多个对象，比如类、函数等。一个包可以包含一个或多个相关模块。包实际上是一个包含一个或多个模块文件的文件夹。因此，如果我们开发的是一个通用的项目，我们可以自己的包用于自己或者他人使用。让我们以创建一个名为 mypackage 的包为例，使用以下步骤：、

1. 30DaysOfPython-zh_CN 文件夹中创建一个名为 mypacakge 的新文件夹
2. 在 mypacakge 文件夹中创建一个空的 **__init__**.py 文件
3. 使用以下代码创建模块arithtic .py和greet.py 

```py
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
```

```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```

最终包的文件夹结构应该是这样的：

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

现在让我们打开python交互式shell并尝试使用自定义包：

```sh
30DaysOfPython-zh-CN > python

>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Mega', 'Qi')
'Mega Qi, welcome to 30DaysOfPython Challenge!'
>>>
```

从上边的例子中可以看出，我们的包可以正常的工作。文件夹包含一个名为 **__init__** 空文件（py的特殊文件——它存储包的内容）。如果我们将 __init__.py 放在包文件夹中，python会将其识别为包。__init__.py 从其模块中公开指定的资源，以便导入到其他python文件中。一个空的__init__.py文件使所有函数在导入包时都可用。总而言之 __init__.py 对于被 Python 识别为包的文件夹是必不可少存在。

### 关于更多包的信息

- 数据库
  - SQLAlchemy or SQLObject - 对几个不同数据库系统的面向对象访问
    - _pip install SQLAlchemy_

- Web开发
  - Django - 高级web框架
    - _pip install django_
  - Flask - 基于Werkzeug的Python微框架
    - _pip install flask_

- HTML爬虫
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - 是一个HTML/XML的解析器，主要的功能也是如何解析和提取HTML/XML数据。
    - _pip install beautifulsoup4_
  - PyQuery - 在Python中实现jQuery;显然比BeautifulSoup快。

- XML 语言
  - ElementTree - Element类型是一种简单但灵活的容器对象，用于在内存中存储层次数据结构，例如简化的XML信息集。注意:Python 2.5及以上版本在标准库中带有ElementTree

- GUI桌面程序
  - PyQt - 跨平台的桌面程序框架
  - TkInter - 传统的Python用户界面工具包（内置）

- 数据分析，数据科学和机器学习
  - Numpy: Numpy(numeric python) 被称为 python 中最受欢迎的机器学习库之一
  - Pandas: 作为数据分析、数据科学和机器学习库，提供高级数据结构和各种各样的分析工具。
  - SciPy: 是一个面向应用程序开发人员和工程师的机器学习库。SciPy库包含优化、线性代数、集成、图像处理和统计模块。
  - Scikit-Learn: 针对Python 编程语言的免费软件机器学习库。通常被认为是处理复杂数据的最佳库之一
  - TensorFlow: 谷歌建立了一个机器学习库
  - Keras: 是一个 Python深度学习框架。

- Network:
  - requests: 一个可以发送请求到服务器(GET, POST, DELETE, PUT)的包
    - _pip install requests_

🌕 你一直在进步，到目前为止你已经成功学习20节内容。真棒！

受限制于练习的海外地址可能服务访问，本篇内容没有明确的练习题，请选择通过搜索引擎学习和练习一些库。

🎉 CONGRATULATIONS ! 🎉

[<< Day 19](../19_Day_File_handling/19_file_handling.md) | [Day 21 >>](../21_Day_Classes_and_objects/21_classes_and_objects.md)
