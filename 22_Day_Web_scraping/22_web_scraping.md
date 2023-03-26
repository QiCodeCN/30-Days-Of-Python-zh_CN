
[<< Day 21](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)


- [📘 Day 22](#-day-22)
  - [Python爬虫](#Python爬虫)
  - [💻 第22天练习](#-第22天练习)

# 📘 Day 22

## Python爬虫

### 什么是数据抓取

互联网上充满了大量的数据，可以应用于不同的目的。为了收集这些数据，我们需要知道如何从一个网站抓取这些数据。

网络抓取本质上是从网站中提取和收集数据，并将其存储在本地机器或数据库中的过程。

在本节中，我们将使用 beautifulsoup 和 requests 包来抓取数据。

**友情提醒：数据抓取不合法，本篇内容请仅用于测试和学习用。**

如果你的Python环境中还没如下两个库，请用pip进行安装。
```sh
pip install requests
pip install beautifulsoup4
```

要从网站抓取数据，需要对HTML标记和CSS选择器有基本的了解。我们使用HTML标签，类或id定位来自网站的内容。

首先导入 requests 和 BeautifulSoup 模块

```py
import requests
from bs4 import BeautifulSoup
```

接着将需要抓取的网页地址赋值给一个url变量，以下我们以手机新浪首页为例子。

```py

import requests
from bs4 import BeautifulSoup
url = 'http://wap.sina.cn/'

# 让我们使用网络请求url，获取返回的数据
response = requests.get(url)
# 检查返回状态，200表示正常
status = response.status_code
print(status)
```

```sh
200
```

使用 beautifulSoup 解析页面内容。

```py
import requests
import re
from bs4 import BeautifulSoup
url = 'http://wap.sina.cn/'

response = requests.get(url)
# 获取请求页面的所有内容
content = response.content
# 加载成beautiful对象
soup = BeautifulSoup(content, 'html.parser')
#解析标题并打印
print(soup.title)
# 获取标题里内容
print("《" + soup.title.get_text() + "》")
# 网站整个页面
# print(soup.body)
# 寻找要闻片段（通过网页右键查看源代码）
yaowen = soup.find(id="yaowen_defense")
# 要闻对象中查找所有<H2>标签，并循环获取概要标题
for h2 in yaowen.find_all('h2'):
    print(h2.contents[0])
```

如果运行这段代码，可以看到提取到了所有的新闻标题。

本节只是抛砖隐喻，并不是python基础学习中核心部分。不过多展开，更多参考官方文档 [beautifulsoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🌕 你如此有能力，每一天都在进步，挑战还剩余8天，加油！本篇内容虽少，但练习不能少。

## 💻 第22天练习

1. 抓取豆瓣电影排行版中电影前10个电影的基本信息 https://movie.douban.com/chart。
2. 从Python网络爬虫靶场 http://www.spiderbuf.cn/ 选择任意一个无反扒的网站进行表数据获取。

🎉 CONGRATULATIONS ! 🎉

[<< Day 21](../21_Day_Web_scraping/21_class_and_object.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)
