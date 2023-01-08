
[<< Day 15](../15_Day_Python_type_errors/15_python_type_errors.md) | [Day 17 >>](../17_Day_Exception_handling/17_exception_handling.md)

- [📘 Day 16](#-day-16)
  - [Python *datetime*](#python-datetime)
    - [获取 *datetime* 信息](#获取-datetime-信息)
    - [使用 *strftime* 格式化日期输出](#使用-strftime-格式化日期输出)
    - [使用 *strptime* 将字符转时间](#使用-strptime-将字符转时间)
    - [使用 *datetime* 模块内*date* ](#使用-datetime-模块内*date* )
    - [时间 *time* 对象](#时间-time-对象)
    - [时间差](#时间差g)
  - [💻 第16天练习](#-第16天练习)
# 📘 Day 16

## Python *datetime*

Python内置有 _datetime_ 模块，可以用来处理日期和时间。在编程的世界里少不了与时间打交到，因此让我们来专门学习一下 _datetime_ 的使用。

```py
>>> import datetime
>>> print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

使用内置 dir 或 help 命令可以打印某个模块中可用的函数。如你所见，在 _datetime_ 模块有很多的方法，不过我们将重点关注其中_date_, _datetime_, _time_ 和 _timedelta_ 这几个。

### 获取 *datetime* 信息

```py
from datetime import datetime
now = datetime.now()
print(now)                      # 当前时间 2023-01-07 20:30:55.689393
day = now.day 
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)  # 日 月 年 小时 秒 7 1 2023 20 30
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 格式化输出时间 7/1/2023, 20:30
```

时间戳或Unix时间戳是UTC时间从1970年1月1日开始的秒数。

### 使用 *strftime* 格式化日期输出

不使用任何内置函数方法的情况，如果我们想输出想要格式日期，我们可能需要这么做：
```py
from datetime import datetime
new_year = datetime(2023, 1, 21)  # 指定日期 2023 除夕
print(new_year)      # 2023-01-21 00:00:00 时间不指定默认0点
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)  #日 月 年 时 分 21 1 2023 0 0
print(f'{year}-{month}-{day} {hour}:{minute}')  # 2023-1-21 0:0
```

然而我们可以使用 *strftime* 更快速方便对时间进行格式化输出， 下面再看一些使用例子：

更新详细的 *strftime* 格式化日期时间方法，可以阅读这 [strftime.org](https://strftime.org/) 网站。

```py
from datetime import datetime
# 获取当前期日和时间
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

time_one = now.strftime("%Y-%m-%d %H:%M:%S")
# YY-dd-mm H:M:S
print("time one:", time_one)

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S
print("time two:", time_two)
```

```sh
time: 20:45:27
time one: 2023-01-07 20:45:27
time two: 07/01/2023, 20:45:27
```

下面的图片展示了_strftime_ 模块所有格式符号。在代码编程中按需使用。

![strftime](../images/day1601_strftime.png)

### 使用 *strptime* 将字符转时间

这里有个建议阅读文档 [documentation](https://www.programiz.com/python-programming/datetime/strptimet)，或许它能帮助你更好的理解。

```py
from datetime import datetime
date_string = "5 March, 2022"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
```

```sh
date_string = 5 March, 2022
date_object = 2022-03-05 00:00:00
```

### 使用 *datetime* 模块内*date* 

```py
from datetime import date
d = date(2022, 5, 1)
print(d)                             # 指定时间 2022-05-01 
print('Current date:', d.today())    # 当前时间 2023-01-07

# 将今天的时间给予today对象
today = date.today()
print("Current year:", today.year)   # 2023
print("Current month:", today.month) # 1
print("Current day:", today.day)     # 7
```

### 时间 *time* 对象

```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute 和 second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute 和 second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(时, 分, 秒, 毫秒)
d = time(10, 30, 50, 200555)
print("d =", d)
```

输出
``` sh  
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555
```

### 时间差

时间可以直接进行差值运算
```py
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
```

使用 *datetime* 模块中 *timedelata* 方便在日期上做加减指定时间单位的加减。

```py
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

```sh
t3 = 86 days, 22:56:50
```

这个 timedelata 需要要结合date或datetime类的对象使用
```py
from datetime import timedelta, date
today = date.today()
print(today)    # 2023-01-07

yestoday = today + timedelta(days=-1)
print(yestoday)  # 2023-01-06
```

🌕 你是如此的努力。你已经在伟大python学习之路上行走了16步了。课后让我们按惯例做些练习吧

## 💻 第16天练习

1. 使用 *datetime* 模块分别获取年、月、日、时、分 和 时间戳信息
2. 使用 `%m/%d/%Y, %H:%M:%S` 格式输出当前时间
3. 如果时间是 “2023年1月1日”，将此字符串时间转成时间类型
4. 计算当前时间和元旦那天的时间差
5. 计算当前时间距离1970年1月1的时间差或时间戳
6. 思考题：想想这个 datetime 模块可以实际应用在那些编码场景中呢？

🎉 CONGRATULATIONS ! 🎉

[<< Day 15](../15_Day_Python_type_errors/15_python_type_errors.md) | [Day 17 >>](../17_Day_Exception_handling/17_exception_handling.md)