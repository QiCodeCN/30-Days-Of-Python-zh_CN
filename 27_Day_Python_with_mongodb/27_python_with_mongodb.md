
[<< Day 26](../26_Day_Python_web/26_python_web.md) | [Day 28 >>](../28_Day_Python_with_mysql/28_python_with_mysql.md)
 
- [📘 Day 27](#-day-27)
- [Python with MongoDB](#python-with-mongodb)
  - [MongoDB](#mongodb)
    - [SQL versus NoSQL](#sql-versus-nosql)
    - [Getting Connection String(MongoDB URI)](#getting-connection-stringmongodb-uri)
    - [Connecting Flask application to MongoDB Cluster](#connecting-flask-application-to-mongodb-cluster)
    - [Creating a database and collection](#creating-a-database-and-collection)
    - [Inserting many documents to collection](#inserting-many-documents-to-collection)
    - [MongoDB Find](#mongodb-find)
    - [Find with Query](#find-with-query)
    - [Find query with modifier](#find-query-with-modifier)
    - [Limiting documents](#limiting-documents)
    - [Find with sort](#find-with-sort)
    - [Update with query](#update-with-query)
    - [Delete Document](#delete-document)
    - [Drop a collection](#drop-a-collection)
  - [💻 Exercises: Day 27](#-exercises-day-27)

# 📘 Day 27

# Python操作数据库

Python是一种后端技术，它可以连接到不同的数据库应用程序。它可以连接到SQL和noSQL数据库。

## MongoDB

MongoDB是一个非关系型数据库。MongoDB将数据存储在类似JSON文档中，这使得MongoDB非常灵活和可扩展。让我们看看SQL和NoSQL数据库的不同术语。下表展示说明SQL和NoSQL数据库之间的区别。


### SQL VS NoSQL

![SQL versus NoSQL](../images/mongoDB/sql-vs-nosql.png)

在本篇中，我们将关注NoSQL数据库中的MongoDB。让我们在[mongoDB](https://www.mongodb.com/)上注册或登录（如果你已经有账号）。


![MongoDB Sign up pages](../images/mongoDB/mongodb-signup-page.png)

如果你是一个新用户，在进入云服务主页后可以点击“Build a Database” 创建一个用于学习目的的在线数据库

![Mongodb free plan](../images/mongoDB/mongodb-free.png)

选择免费服务类型，选择地区，并给定一个服务名称

![Mongodb cluster name](../images/mongoDB/mongodb-cluster-name.png)

现在，创建了一个免费的空间。创建新的空间服务可能会需要一定时间部署。

![Mongodb sandbox](../images/mongoDB/mongodb-sandbox.png)

添加一个直连IP地址 “Add Your Current IP address”

![Mongodb allow ip access](../images/mongoDB/mongodb-allow-ip-access.png)

添加一个账户密码，首个将作为管理员账号，请牢记。再次添加时候会可以选择用户权限。

![Mongodb add user](../images/mongoDB/mongodb-add-user.png)

以上两个创建成功后，点击“Choose a connection method”进入下一步

![Mongodb create uri](../images/mongoDB/mongodb-create-uri.png)

选择驱动版本 Python 3.6 or later，本复制连接到粘贴板或者本地文件中备用。

![Mongodb python driver](../images/mongoDB/mongodb-python-driver.png)

### 取得连接字符串(MongoDB URI)

刚才拷贝的连接字符串类似，它将是你Python程序连接的MongoDB的URL，但请注意账号密码要替换成你自己刚才创建的。

```sh
mongodb+srv://MegaQi:<password>@30dayofpython.nax3k0s.mongodb.net/?retryWrites=true&w=majority
```

Python需要一个mongoDB驱动程序来访问mongoDB数据库。我们将使用 _pymongo_ 模块 将我们应用程序与mongoDB连接起来。在你的项目目录中首先你需要安装pymongo和dnspython。

```sh
pip install pymongo
```

### 连接尝试

出于可能出现国内网络原因，如果你连接云服务有问题，可以下载安装包本地装一个MongoDB方便学习测试。

下载地址：ww.mongodb.com/download-center/community

![mongodb](../images/mongoDB/mongodb-download.png)

使用 pymongo 对数据进行连接(以下均为本地数据演示)
```py
import pymongo
# client = pymongo.MongoClient("mongodb+srv://MegaQi:YourPassword@30dayofpython.dhy8xao.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/") # 注意，本地mongo数据库安装完后默认是没有用户密码的可直连
print(client.list_database_names())
```

当我们运行上面的代码时，我们得到默认的mongoDB数据库。

```sh
['admin', 'config', 'local']
```

如果你是一个完整安装，你的电脑里还有个桌面客户端compass用于连接数据。

![compass](../images/mongoDB/mongodb-compass.png)

### 创建数据库和集合

让我们创建一个名为 _thirty_days_of_python_ 数据库和 _students_ 集合。

要创建一个数据库可以选择以下两种方式中一种
```sh
db = client.name_of_databse
# 或
db = client['name_of_database']
```
在如下代码中在创建数据的同时，通过db.collection.insert_one 再插入一条数据，这样数据就会被成功创建。
```py
import pymongo
# client = pymongo.MongoClient("mongodb+srv://MegaQi:YourPassword@30dayofpython.dhy8xao.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

db = client.thirty_days_of_python

db.students.insert_one({'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18})
print(client.list_database_names())
```

现在，已经创建了数据库 *thirty_days_of_python* 和 *students* 的集合。当我们再次检查数据库列表的时候就会发现新增的 *thirty_days_of_python* 数据了。

```sh
['admin', 'config', 'local', 'thirty_days_of_python']
```

这时你可以通过云服务Collections或本地客户端查看最新的数据，如果存在students说明，数据库和文档都成功创建了。

![Creating database and collection](../images/mongoDB/mongodb-creating_database.png)

从图中可以看出，创建文档时使用了一个长id，该id为主键。每次我们创建一个文档，mongoDB都会为它创建一个唯一的id。

### Inserting many documents to collection

上述方法 *insert_one()* 每次仅插入一项，如果我们想一次插入多条数据，可以使用 *insert_many()* 方法或for循环。

例子1：我们可以使用for循环一次插入多个文档。

```py
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
    ]
for student in students:
    db.students.insert_one(student)
```

例子2：使用 insert_many 以此插入多条。
```py
students2 = [
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
        {'name':'Tom','country':'Kroen','city':'Seoul','age':26},
    ]
db.students.insert_many(students2)
```

当执行这块代码无异常后，查看数据结果如下：

![insert](../images/mongoDB/mongodb-insert.png)

### MongoDB查找

关于文档查找，可以使用 *find()* 和 *find_one()* 方法，这两是mongoDB数据库中查找集合数据的常用方法。它类似于MySQL数据库中的SELECT语句。

让我们先使用 _find_one()_ 方法来获取数据库集合中的文档，如果有符合条件的多条，默认返回第一条。

- \*find_one({"\_id": ObjectId("id"})

```py
student_one = db.students.find_one()  #不指定条件则默认返回默认排序第一条
print(student_one)

```

```sh
{'_id': ObjectId('64295174e77a296584fc6660'), 'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
```

上面的查询返回第一个条目，但是我们可以使用特定的\_id针对特定的文档。举个例子，用David的id获取David对象。

- '\_id':ObjectId('64296b238e322f5f0a57da4b')

```py
from bson.objectid import ObjectId # ID需要使用ObjectId对象

student_with_id = db.students.find_one({'_id':ObjectId('64296b238e322f5f0a57da4b')})
print(student_with_id)
```

```sh
{'_id': ObjectId('64296b238e322f5f0a57da4b'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
```

我们已经通过上面的例子看到了如何使用 _find_one()_。让我们来看看如何使用 _find()_

- _find()_: 如果不传递查询对象，则返回集合中的所有数据。

```py
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['thirty_days_of_python'] # 换一种访问数据库的方式
students = db.students.find()
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('64295174e77a296584fc6660'), 'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
{'_id': ObjectId('64296b238e322f5f0a57da4a'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('64296b238e322f5f0a57da4b'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('64296c03dcde19198344b720'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('64296c03dcde19198344b721'), 'name': 'Tom', 'country': 'Kroen', 'city': 'Seoul', 'age': 26}
```

我们可以通过在 _find({}，{})_ 中传递第二个对象来指定要返回的字段。0表示不包含，1表示包含。

```py
students = db.students.find({}, {"_id":0,  "name": 1, "country":1})
for student in students:
    print(student)
```
仅仅返回了指定显示的name和country字段
```sh
{'name': 'MegaQi', 'country': 'China'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
{'name': 'Tom', 'country': 'Kroen'}
```

### 条件查找

在mongoDB想要通过条件进行查找。我们可以传递一个查询对象实现对文档的过滤。

```py
query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)
```
指定国家为 **Finland** 条件
```sh
{'_id': ObjectId('64296c03dcde19198344b720'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### 多条件查询

```py
query = {
    "country":"China",
    "city":"ShangHai"
}
students = db.students.find(query,{"_id":0,  "name": 1, "country":1, "city":1})
for student in students:
    print(student)
```

```sh
{'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai'}
```

### 带有修饰符的查询

```py
query = {"age":{"$gt":27}} # $gt 表示大于
students = db.students.find(query)
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('64296b238e322f5f0a57da4a'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('64296b238e322f5f0a57da4b'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
```

其他一些条件符号常用的还有：
- $eq = (等于)
- $gt > (大于)
- $gte >= (大于等于)
- $lt < (小于)
- $lte <= (小于等于)
- $ne != (不等于)
- $in in (in)
- $nin !in (not in)

### 限制返回数量

可以使用 _limit()_ 方法限制返回的文档数量。同mysql中的limit语法。

```py
student_limit_three = db.students.find().limit(3)
for student in student_limit_three:
    print(student)
```
所有查询数据的前三条
```sh
{'_id': ObjectId('64295174e77a296584fc6660'), 'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
{'_id': ObjectId('64296b238e322f5f0a57da4a'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('64296b238e322f5f0a57da4b'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
```

### 排序查询

默认情况下，排序是升序的。我们可以通过添加-1参数将排序改为降序。

```py
students = db.students.find().sort('name')
print(">>>姓名正序：")
for student in students:
    print(student)


students = db.students.find().sort('name',-1)
print(">>>姓名倒序：")
for student in students:
    print(student)

students = db.students.find({},{"_id":0, "age": 1, "name": 1, "country":1, "city":1}).sort('age')
print(">>>姓名小到大：")
for student in students:
    print(student)

students = db.students.find({},{"_id":0, "age": 1, "name": 1, "country":1, "city":1}).sort('age',-1)
print(">>>年龄大到小：")
for student in students:
    print(student)
```

Ascending order

```sh
>>>姓名正序：
>>>姓名正序：
{'_id': ObjectId('64296b238e322f5f0a57da4a'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('64296b238e322f5f0a57da4b'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('64295174e77a296584fc6660'), 'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
{'_id': ObjectId('64296c03dcde19198344b720'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('64296c03dcde19198344b721'), 'name': 'Tom', 'country': 'Kroen', 'city': 'Seoul', 'age': 26}
>>>姓名倒序：
{'_id': ObjectId('64296c03dcde19198344b721'), 'name': 'Tom', 'country': 'Kroen', 'city': 'Seoul', 'age': 26}
{'_id': ObjectId('64296c03dcde19198344b720'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('64295174e77a296584fc6660'), 'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
{'_id': ObjectId('64296b238e322f5f0a57da4b'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('64296b238e322f5f0a57da4a'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
>>>姓名小到大：
{'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
{'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'name': 'Tom', 'country': 'Kroen', 'city': 'Seoul', 'age': 26}
{'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
>>>年龄大到小：
{'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'name': 'Tom', 'country': 'Kroen', 'city': 'Seoul', 'age': 26}
{'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
```

### 查询更新

我们将使用 *update_one()* 方法来更新一项数据。它需要两个对象，一个是查询对象，另一个是新的对象。

```py
import pymongo
from bson.objectid import ObjectId
# client = pymongo.MongoClient("mongodb+srv://MegaQi:YourPassword@30dayofpython.dhy8xao.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['thirty_days_of_python']

query = {'age':34}
new_value = {'$set':{'age':22}}
db.students.update_one(query, new_value)

for student in db.students.find():
    print(student)
```

```sh
{'_id': ObjectId('64295174e77a296584fc6660'), 'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
{'_id': ObjectId('64296b238e322f5f0a57da4a'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 22}
{'_id': ObjectId('64296b238e322f5f0a57da4b'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('64296c03dcde19198344b720'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('64296c03dcde19198344b721'), 'name': 'Tom', 'country': 'Kroen', 'city': 'Seoul', 'age': 26}
```

当我们想要批量更改文档数据时，可以使用 *upate_many()* 方法。

### 删除文档数据
方法 *delete_one()* 用于删除一个文档。*delete_one()* 需要一个查询对象参数。它只会删除第一个符合条件的文档。

让我们从集合中删除一个名为John的文档。

```py
query = {'name':'John'}
db.students.delete_one(query)
for student in db.students.find():
    print(student)

```
数据减少了一条，John的文档信息被移除了。
```sh
{'_id': ObjectId('64295174e77a296584fc6660'), 'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
{'_id': ObjectId('64296b238e322f5f0a57da4a'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 22}
{'_id': ObjectId('64296c03dcde19198344b720'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('64296c03dcde19198344b721'), 'name': 'Tom', 'country': 'Kroen', 'city': 'Seoul', 'age': 26}
```

同样，当我们向做批量删除的时候，可以使用 *delete_many()* 方法，它也需要一个查询对象。另外如果想直接清空这个文档，可以将查询条件置为空，即 *delete_many({})*

### 删除集合

我们可以使用 _drop()_ 方法从数据里直接删除一个集合。

```py
db.students.drop()

for student in db.students.find():
    print(student)

```
现在我们已经将学生文档集从数据中删除掉了。再次查询打印将输出的是空的结果。

以上是对于数据库MongoDB的一些基本用法。

本篇没有额外的作业，大家只需要按需了解文档数据库MongoDB的云（或本地）服务使用，及基本的语法即可。


🎉 CONGRATULATIONS ! 🎉

[<< Day 26](../26_Day_Python_web/26_python_web.md) | [Day 28 >>](../28_Day_Python_with_mysql/28_python_with_mysql.md)
