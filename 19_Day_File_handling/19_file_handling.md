
[<< Day 18](../18_Day_Regular_expressions/18_regular_expressions.md) | [Day 20 >>](../20_Day_Python_package_manager/20_python_package_manager.md)

- [📘 Day 19](#-day-19)
  - [文件处理](#文件处理)
    - [读(r)模式](#读(r)模式)
    - [文件写入和更新](#文件写入和更新)
    - [删除文件](#删除文件)
  - [文件类型](#文件类型)
    - [.txt](#.txt)
    - [.json](#.json)
    - [JSON转字典](#JSON转字典)
    - [字典转JSON](#字典转JSON)
    - [保存为JSON文件](#保存为JSON文件)
    - [.csv](#.csv)
    - [.xlsx](#.xlsx)
    - [.xml](#.xml)
  - [💻 第19天练习](#第19天练习)
    - [练习1级](#练习1级)
    - [练习2级](#练习2级)
    - [练习3级](#练习3级)

# 📘 Day 19

## 文件处理

此前我们已经见过了不同的Python数据类型。通常也会将我们的数据存储在不同的格式的文件中。在这章节中我们将学习如何处理这些不同的类型的文件（.txt, .json, .xml, .csv, .tsv, .excel）。首先，让我们从最熟悉的txt类型文件开始。

文件处理是程序中很重要的部分，它允许我们进行创建、读取、更新和删除。在Python中处理文件数据使用的是 _open_ 内置方法。

```py
# 语法形式
open('filename', mode) # 模式mode(r, a, w, x, t,b)  表示 读, 写, 更新
```

- "r" - 英文Read表示读 - 默认值。以读的模式打开一个文件，如果文件不存在它将返回一个错误。Opens a file for reading, it returns an error if the file does not exist
- "a" - 英文Append表示追加 - 以追加模式打开文件，如果文件不存在则会自动创建。Opens a file for appending, creates the file if it does not exist
- "w" - 英文Write表示写 - 以写的模式打开一个文件，如果文件不存在则创建。Opens a file for writing, creates the file if it does not exist
- "x" - 英文Create表示创建 - Creates the specified file, returns an error if the file exists
- "t" - 英文Text表示文本 - Default value. Text mode
- "b" - 英文Binary表示字节 - Binary mode (e.g. images)

### 读(r)模式

方法 _open_ 默认模式是只读模式，因此我们可以不需要特别的指定mode= ‘r’ 或 ‘rt’。注意，我已经创建好了一个文件名为 “reading_file_example.txt” 的文件在项目的files目录下。让我们来看看如何读取它。

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='cp936'>>
```
正如你在例子中看到的，我通过open打开一个文件，并打印了一些加载文件后的一些信息。其中读取文件内容会有几种方法：_read()_, _readline_, _readlines_。关闭文件使用 _close()_ 方法。

- _read()_：将整个文件内容以字符字符串的形式读取。其中如果我们想限制读取的字符，我们可以给定一个整数类型值 *read(number)* 。

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# 读取文件全部内容的输出
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.I love python
```

让我们指定数量字符读取，比如从文件中读取10个字符。

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# 指定读取数量输出
<class 'str'>
This is an
```

- _readline()_: 读取一行，当第一调用的时候默认为第一行，再次读取依次读取下一行。

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)  # 第一行

print(f.readline())  # 第二行
print(f.readline())  # 因为文件中只用两行所以当尝试第三次readline时候返回是空字符串

f.close()
```

- _readlines()_: 按行的形式读取所有文本，并且返回一个字符行列表。

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# readlines测试输出
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.I love python']
```

还有另外一种列表行读取文本的方式是使用 _splitlines()_:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# splitlines 输出
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
# 两种方式大家可以注意下返回的行列表有什么区别？是的第二种方式不包含 \n 换行符。
```

当打开一个文件，使用完的时候必须关闭它。其实有一种更高级的方式处理它。我们可以使用  _with_ ，此方式可以自己关闭文件使用。看下一下方法应用的例子：

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# 实际输出
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### 文件写入和更新

如果想向一个已经存在文件写入内容，我们必须在使用 _open()_ 方法时候添加一个参数模式：

- "a" - append 追加 - 将在文件默认追加内容，如果文件不存在将自动创建一个新的文件。
- "w" - write 写 - 覆盖模式写入内容，如果文件不存在则会创建。

接下来让我们将一些文本添加已经读取的文件中：

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

用文本编辑器打开 reading_file_example.txt 看是否将内容写入到了文件末尾。

```py
with open('./files/writing_file_example.txt',mode='w', encoding="utf-8") as f:
    f.write('写入文件测试，其中还需要指定字符编码，否则中文会乱码。')
```

### 删除文件

在之前的篇幅中，我们知道了怎么通过 _os_ 创建一个目录或者文件。现在，我我们看看如何通过它删除一个文件。 

```py
import os
os.remove('./files/example.txt')

```

如果删除的文件不存在，它会返回一个错误，因此一个好的编程应该加一个判断，像这样：

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('删除的文件不存在')
```

## 文件类型

### .txt

带有txt扩展名的文件是最常见的一种数据格式文件，这部分我们已经在上边的一节中讲过了。让我们接下来看一个 JSON 文件。

### .json

JSON代表JavaScript对象表示法。实际上，它是一个字符串化的JavaScript对象或Python字典。

_Example:_

```py
# 字典
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}

# JSON: 一个字典格式的字符串
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# 我们使用三个引号表示多行字符串，让它更具有可读性
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### JSON转字典

将JSON转成字典，首先我们需要导入 _json_ 模块，然后使用 _loads_ 方法。

```py
import json
# JSON
person_json = '''{
    "name": "MegaQi",
    "country": "China",
    "city": "ShangHai",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# 接下来 json 转 dict 
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

预期输出
```sh
<class 'dict'>
{'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'skills': ['JavaScrip', 'React', 'Python']}
MegaQi
```

### 字典转JSON

反过来，如果想将字典转成json类型，我们需要使用 json 模块中的 _dumps_ 方法。

```py
import json
# python 字典
person = {
    "name": "MegaQi",
    "country": "China",
    "city": "ShangHai",
    "skills": ["JavaScrip", "React", "Python"]
}

# 转成json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
```

预期输出
```sh
# 需要注意的是，当你打印json的时候，它并没有引号。
# JSON并不是一种特殊类型, 实际上它在python中就是字符串.
<class 'str'>
{
    "name": "MegaQi",
    "country": "China",
    "city": "ShangHai",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
```

### 保存为JSON文件

我们也可以将数据保存为json文件。对于编写json文件，我们使用 _json.dump()_ 方法，它可以接受字典，输出到文件，ensure_ascii和缩进。

```py
import json
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

```
注意：想输出真正的中文需要指定 ensure_ascii=False，因为json.dumps 序列化时对中文默认使用的ascii编码
``` py
print(json.dumps('{"language":"中文"}'))   # "{\"language\":\"\u4e2d\u6587\"}"
print(json.dumps('{"language":"中文"}', ensure_ascii=False))  # "{\"language\":\"中文\"}"

```

在上面的代码中，我们使用了编码和缩进让json文件易于阅读。

### .csv

CSV代表逗号分隔的值。CSV是一种简单的文件格式，用于存储表格数据，如电子表格或数据库。CSV是数据科学中非常常见的数据格式。

**例子数据:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**例子演示**
这里我们借助csv模块来读取csv文件
```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') 
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

执行代码输出:
```sh
Column names are :name, country, city, skills
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines:  2
```

### .xlsx

如果要读取excel文件，我们需要安装 _xlrd_ 包。可以通过终端 `pip install xlrd` 进行安装，至于pip包管理的更多使用，我们将在下一篇中覆盖。

```py
import xlrd  # xlsx格式需要用openpyxl库
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### .xml
XML是另一种看起来像HTML的结构化数据格式。在XML中，标记不是预先定义的。第一行是一个XML声明。person标记是XML的根，并且有性别属性。
XML is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute.

**XML文件数据**
```xml
<?xml version="1.0"?>
<person gender="男">
  <name>MegaQi</name>
  <country>China</country>
  <city>ShangHai</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

关于xml更多的操作请自行按需需求，这里只做个简单演示。

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```
代码执行后输出： 
```sh
Root tag: person
Attribute: {'gender': '男'}
field:  name
field:  country
field:  city
field:  skills
```

🌕 你取得了很大的进步。保持这样的势头，加油加油加油！下面让我们来做一些练习吧。

## 💻 第19天练习

### 练习1级
1. 写一个给定参数文件和个数的方法，然后统计文件文本单词和数量，最后按照指定个数返回。练习用的所有文件在项目源码 data 目录下。
- a) 读取 obama_speech.txt 文件，进行方法调用
- b) 打开 michelle_obama_speech.txt 文件，进行方法调用
- c) 读取 donald_speech.txt 文件，进行方法调用
- d) 打开 melina_trump_speech.txt，进行方法调用

2. 从data目录中读取 countries_data.json 文件，并且创建一个方法，实现返回指定个数口最多的国家。


### 练习2级

1. 从文件email_exchange_big.txt中提取所有传电子邮件地址，并作为列表类型。

2. 找出英语中最常用的单词。将函数名命名为find_most_common_words，它将接受两个参数：一个字符串或一个文件和一个正整数（表示列表个数）。函数将返回一个按降序排列的元组数组。参考输出

3. 定义方法 find_most_frequent_words 实现文件的中最多单词的统计。分别用如下文件：
- /data/obama_speech.txt 前10
- /data/michelle_obama_speech.txt 前10
- /daa/donald_speech.txt 前10
- /data/melina_trump_speech.txt 前10

4. 读取文件/data/hacker_news.csv 文件，然后找出：
- 统计包含python或Python行数
- 统计包含JavaScript, javascript or Javascript行数
- 统计包含Java但不包含JavaScript的行数

🎉 CONGRATULATIONS ! 🎉

[<< Day 18](../18_Day_Regular_expressions/18_regular_expressions.md) | [Day 20 >>](../20_Day_Python_package_manager/20_python_package_manager.md)
