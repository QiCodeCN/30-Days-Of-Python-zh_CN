
[<< Day 24](../24_Day_Statistics/24_statistics.md) | [Day 26 >>](../26_Day_Python_web/26_python_web.md)

- [📘 Day 25](#-day-25)
  - [Pandas](#pandas)
  - [DataFrames](#dataframes)
  - [使用Pandas读取CSV文件](#使用Pandas读取CSV文件)
  - [编辑 DataFrame](#编辑-DataFrame)
  - [检查列值的数据类型](#检查列值的数据类型)
  - [💻 第25天练习](#💻-第25天练习)
  
# 📘 Day 25

## Pandas

Pandas是Python程序语言中一种开源、高性能、易于使用的数据结构和数据分析工具。
Pandas添加了数据结构和工具，用于处理类似表格的数据，即 *Series* 和 *Data Frames*。
它主要提供了数据操作工具有：
- reshaping
- merging
- sorting
- slicing
- aggregation
- imputation

### 安装pandas包

```py
conda install pandas
```

Pandas数据结构基于 *Series* 和 *DataFrames*。 

一个 *series* 是一个 *column*，一个DataFrame是一个由*series* 集合组成的*多维表* 。为了创建pandas *series*，我们使用numpy来创建一个一维数组或python列表。

首先让我们看下 *series* 例子:

Names Pandas Series

![pandas series](../images/day2501_pandas-series-1.png) 

Countries Series

![pandas series](../images/day2502_pandas-series-2.png) 

Cities Series

![pandas series](../images/day2503_pandas-series-3.png)

如您所见，pandas系列只是一列数据。如果我们想要有多个列，我们使用 *data frames*。下面的例子展示了pandas数据框架。

![Pandas data frame](../images/day2504_pandas-dataframe-1.png)

*DataFrame* 是行和列的集合。请看下面的表格,它比上面的例子有更多的表列:

![Pandas data frame](../images/day2505_pandas-dataframe-2.png)

接下来，我们将了解如何导入pandas，以及如何使用pandas创建 *Series* 和 *dataframe*

### 引入 Pandas

```python
import pandas as pd
import numpy  as np
```

### 创建默认索引的Pandas Series

```python
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)
```
默认索引从0开始
```sh
0    1
1    2
2    3
3    4
4    5
dtype: int64
```

### 创建自定义索引的Pandas Series
示例1：
```python
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5]) # 指定索引1-5
print(s)
```

```sh
    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64

```
示例2
```python
fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3]) # 指定索引1-3，列值类型object
print(fruits)
```

```sh
1    Orange
2    Banana
3     Mango
dtype: object
```

### 从字典创建Pandas Series

```python
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)
```
行索引为字典key
```sh
name       Asabeneh
country     Finland
city       Helsinki
dtype: object
```

### 创造一个常量Pandas Series

```python
s = pd.Series(10, index = [1, 2, 3])
print(s)
```
```sh
1    10
2    10
3    10
dtype: int64
```

### 使用Linspace创建Pandas Series
Linspace 表示线性等分向量

```python
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None,axis=0)
# 参数 num 表示样本数量
s = pd.Series(np.linspace(5, 20, 10))
print(s)
```

```sh
0     5.000000
1     6.666667
2     8.333333
3    10.000000
4    11.666667
5    13.333333
6    15.000000
7    16.666667
8    18.333333
9    20.000000
dtype: float64
```

## DataFrames

Pandas DataFrames 可以通过以下不同的方式进行创建

### 从二维列表中创建

```python
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)
```

```
      Names  Country       City
0  Asabeneh  Finland    Helsink
1     David       UK     London
2      John   Sweden  Stockholm
```

### 从Dict字典创建

```python
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)
```

```
      Name  Country       City
0  Asabeneh  Finland    Helsiki
1     David       UK     London
2      John   Sweden  Stockholm
```

### 从列表字典创建

```python
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
```

```
       Name  Country       City
0  Asabeneh  Finland   Helsinki
1     David       UK     London
2      John   Sweden  Stockholm
```

## 使用Pandas读取CSV文件

在此项目中的 /data/weight-height.csv 找到示例文件

```python
import pandas as pd

df = pd.read_csv('./data/weight-height.csv')
print(df)
```
```sh
      Gender     Height      Weight
0       Male  73.847017  241.893563
1       Male  68.781904  162.310473
2       Male  74.110105  212.740856
3       Male  71.730978  220.042470
4       Male  69.881796  206.349801
...      ...        ...         ...
9995  Female  66.172652  136.777454
9996  Female  67.067155  170.867906
9997  Female  63.867992  128.475319
9998  Female  69.034243  163.852461
9999  Female  61.944246  113.649103

[10000 rows x 3 columns]
```

### 数据探索

让我们使用 *head()* 只读取前5行

```python
# head(self: NDFrameT, n: int = 5)
print(df.head()) 
```
不指定行数默认前5行
```
  Gender     Height      Weight
0   Male  73.847017  241.893563
1   Male  68.781904  162.310473
2   Male  74.110105  212.740856
3   Male  71.730978  220.042470
4   Male  69.881796  206.349801
```

让我们学习使用 *tail()* 方法来获取数据表的尾部行。

```python
# tail(self: NDFrameT, n: int = 5)
print(df.tail()) 
```
```
9995  Female  66.172652  136.777454
9996  Female  67.067155  170.867906
9997  Female  63.867992  128.475319
9998  Female  69.034243  163.852461
9999  Female  61.944246  113.649103
```

正如您所看到的csv文件有3列：性别、身高和体重。并且1000行，如果 *DataFrame* 有很多行列，我们就需要一种方法来知晓行列数据，对此我们使用 *shape* 方法。

```python
df = pd.read_csv('./data/weight-height.csv')
print(df.shape)
# (10000, 3)
```

使用 *columns* 方法获得所有列,返回列头。

```python
print(df.columns)
# Index(['Gender', 'Height', 'Weight'], dtype='object')
```


现在，让我们使用列Key获取一个特定的列

```python
heights = df['Height']  # 现在它成为一个 series
print(heights) 
```

```sh
0       73.847017
1       68.781904
2       74.110105
3       71.730978
4       69.881796
          ...
9995    66.172652
9996    67.067155
9997    63.867992
9998    69.034243
9999    61.944246
Name: Height, Length: 10000, dtype: float64
```

其他列如法炮制均可通过列头关键词获取一列值

接下来我们再来了解下 *describe()*方法，它提供数据集的一些描述性统计值。

```python
print(heights.describe()) # 给出关于身高列的一些统计信息
```

```sh
count    10000.000000
mean        66.367560
std          3.847528
min         54.263133
25%         63.505620
50%         66.318070
75%         69.174262
max         78.998742
Name: Height, dtype: float64
```

```python
print(df.describe())  # 对整个dataFrame的统计信息
```

```
             Height        Weight
count  10000.000000  10000.000000
mean      66.367560    161.440357
std        3.847528     32.108439
min       54.263133     64.700127
25%       63.505620    135.818051
50%       66.318070    161.212928
75%       69.174262    187.169525
max       78.998742    269.989699
```

类似 *describe()*, 还有 *info()* 方法同样也给出关于数据集的一些统计。

## 编辑 DataFrame

维护 DataFrame 我们可以：
- 创建一个新的 DataFrame
- 创建一个新的列到 DataFrame
- 从 DataFrame 移除一个存在列
- 修改一个存在 DataFrame 的列
- 改变 DataFrame 列的数据类型


### 创建

像往常一样，首先我们要导入依赖包。现在，让我们导入pandas和numpy，通常它俩是和好的组合。

```python
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
```

``` sh
       Name  Country       City
0  Asabeneh  Finland   Helsinki
1     David       UK     London
2      John   Sweden  Stockholm
```

如果想向DataFrame中添加列，可以像向字典中添加键一样操作。

### 添加列

让我们像其上边的姓名国家和城市的DataFrame添加一列体重信息

```python
weights = [74, 78, 69]
df['Weight'] = weights
print(df)
```

``` sh
       Name  Country       City  Weight
0  Asabeneh  Finland   Helsinki      74
1     David       UK     London      78
2      John   Sweden  Stockholm      69
```

最后再向其 DataFrame 添加一份身高信息

```python
heights = [173, 175, 169]
df['Height'] = heights
print(df)
```

``` sh
       Name  Country       City  Weight  Height
0  Asabeneh  Finland   Helsinki      74     173
1     David       UK     London      78     175
2      John   Sweden  Stockholm      69     169
```

在上边的例子中，我们添加了体重和身高两个新列。接下来让我们看下如何改变值。

### 修改列值
直接对其整列进行操作，比如对身高单位换成米单位值
```python
df['Height'] = df['Height'] * 0.01
print(df)
```

``` sh
       Name  Country       City  Weight  Height
0  Asabeneh  Finland   Helsinki      74    1.73
1     David       UK     London      78    1.75
2      John   Sweden  Stockholm      69    1.69
```

接下来我们再新增一列BMI（Body Mass Index），它表示身体质量指数，计算公式为：BMI=体重÷身高²。
```python
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()
df['BMI'] = bmi
print(df)
```
使用函数可以使我们的代码更简洁，但是不使用函数也可以计算bmi
``` python
df['BMI'] = df['Weight'] / (df['Height'] * df['Height'])
print(df)
```
以上两种方式的结果一样如下：
``` sh
       Name  Country       City  Weight  Height        BMI
0  Asabeneh  Finland   Helsinki      74    1.73  24.725183
1     David       UK     London      78    1.75  25.469388
2      John   Sweden  Stockholm      69    1.69  24.158818
```

### 格式化

DataFrame的BMI列值是浮点数，让我们格式化一下仅保留一位小数。

```python
df['BMI'] = round(df['BMI'], 1)
print(df)
```

``` sh
0  Asabeneh  Finland   Helsinki      74    1.73  24.7
1     David       UK     London      78    1.75  25.5
2      John   Sweden  Stockholm      69    1.69  24.2
```

DataFrame中的信息似乎还不太完整，让我们再继续添加出生年份和当前年份两列。


```python
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2023, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)
```

```sh
       Name  Country       City  Weight  Height   BMI Birth Year  Current Year
0  Asabeneh  Finland   Helsinki      74    1.73  24.7       1769          2023
1     David       UK     London      78    1.75  25.5       1985          2023
2      John   Sweden  Stockholm      69    1.69  24.2       1990          2023
```

## 检查列值的数据类型

```python
print(df.Weight.dtype)
```

```sh
int64
```

```python
print(df['Birth Year'].dtype) 

```
它给出类型是字符串对象，让我们来把它改为整数类型
```python
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) 
```

```sh
int32
```

同样，我们对年份也改下对应的列数值类型

```python
df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)
```

```sh
dtype('int32')
```

现在，出生年份和当前年份的列值是整数。我们接下来就可以计算其年龄了。

```python
ages = df['Current Year'] - df['Birth Year']
print(ages)
```
```
0    254
1     38
2     33
dtype: int32
```
最后将计算后的年龄列追加到dataframe数据中
```python
df['Ages'] = ages
print(df)
```

```
       Name  Country       City  Weight  Height   BMI  Birth Year  Current Year  Ages
0  Asabeneh  Finland   Helsinki      74    1.73  24.7        1769          2023   254
1     David       UK     London      78    1.75  25.5        1985          2023    38
2      John   Sweden  Stockholm      69    1.69  24.2        1990          2023    33
```

请注意，第一行值中年龄足有254岁，人是不可能活那么久的，这里只是为了演示和为下边的判断操作做铺垫。

### 布尔索引

过滤出年龄大于120的数据
```python
print(df[df['Ages'] > 120])
```

```
       Name  Country      City  Weight  Height   BMI  Birth Year  Current Year  Ages
0  Asabeneh  Finland  Helsinki      74    1.73  24.7        1769          2023   254
```

查看年龄小于120的数据
```python
print(df[df['Ages'] < 120])
```

```
    Name Country       City  Weight  Height   BMI  Birth Year  Current Year  Ages
1  David      UK     London      78    1.75  25.5        1985          2023    38
2   John  Sweden  Stockholm      69    1.69  24.2        1990          2023    33
```

## 💻 第25天练习

1. 从数据目录中读取 /data/hacker_news.csv 文件
2. 获取前5行数据
3. 获取最后5行数据
4. 获得标题，数据作为一个pandas series返回
5. 计算这个dataframe的行和列个数
    - 过滤包含python的标题
    - 过滤包含JavaScript的标题
    - 尝试对数据做一些增改计算格式化等操作

🎉 CONGRATULATIONS ! 🎉

[<< Day 24](../24_Day_Statistics/24_statistics.md) | [Day 26 >>](../26_Day_Python_web/26_python_web.md)
