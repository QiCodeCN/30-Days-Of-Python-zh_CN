
import requests
import re
from bs4 import BeautifulSoup

def move_top():
    url = 'https://movie.douban.com/chart'

    # 这里需要增加header模拟是浏览器请求，否者会没有内容返回
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all(class_='item')
    top_num = 1
    for item in items:
        print(f"===TOP{top_num}===")
        print("电影名：", item.find('img')["alt"])
        print("参演员：", item.find('p',class_='pl').contents[0])
        print("评  分：", item.find('span',class_='rating_nums').contents[0])
        if top_num > 10:
            break
        print("\n")
        top_num = top_num + 1

    
    # 练习1：豆瓣高分电影爬取前10    
    move_top()

    # 练习2：自选推荐靶场练习
    # 参考答案略，比较感兴趣的自行深入研究下
