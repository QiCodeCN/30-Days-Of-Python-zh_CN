import json
import re
import os
import csv

# 参考练习day18的正则的字符统计，抽象出一个公共方法
def word_count_sort(data):
    words = re.findall(r'\w+', data) 

    word_dict = dict()  # 通过字典统计
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    word_tuple = [(v, k) for k,v in word_dict.items()]  #转元组list
    word_sort = sorted(word_tuple, reverse=True)  # 内置排序
    return word_sort

# 1.1 统计单词数量，按照指定前多少返回，方法名可以命名为 most_words
def most_words_in_file(filename, num):
    with open(filename, encoding='utf-8') as f:
        txt_data = f.read()
    
    sort_word = word_count_sort(txt_data)
    return sort_word[:num]

# print(most_words_in_file(filename='./data/obama_speech.txt', num=10))
# print(most_words_in_file(filename='./data/donald_speech.txt', num=5))

# 1.2 读取 countries_data.json 返回指定个数口最多的国家
def most_populated_countries(filename, num):
    with open(filename) as f:
        js_data = json.loads(f.read())
    
    js_data.sort(key=lambda x: (x['population']), reverse=True)
    return js_data[:num]

# print(most_populated_countries(filename='./data/countries_data.json', num=10))
# print(most_populated_countries(filename='./data/countries_data.json', num=3))

# 2.1 从文件email_exchange_big.txt中提取所有传电子邮件地址，并作为列表类型。
def get_email_list(filename):
    with open(filename) as f:
        data = f.read()

    emails = re.findall(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?", data) 
    return list(set(emails))

# print(get_email_list('./data/email_exchanges.txt'))
# print(get_email_list('./data/email_exchanges_big.txt'))

# 2.2 定义 find_most_common_words 方法，从指定参数中读取字符或文件，返回排序后的指定个数元组
def find_most_common_words(data, num, ftype="file"):
    if ftype == "file":
        if not os.path.exists(data):
            return "文件不存在"
        
        with open(data, encoding="utf-8") as f:
            read_data = f.read()
        words = word_count_sort(data=read_data)

    else:
        words = word_count_sort(data=data)
    return words[:num]

# print(find_most_common_words(data='./data/donald_speech.txt', num=3, ftype="file"))
# print(find_most_common_words(data='./data/donald_speech.txt', num=3, ftype="str"))

# 2.3 定义方法 find_most_frequent_words 实现文件的中最多单词的统计。
# 此题和上边类似，略

# 2.4 读取文件/data/hacker_news.csv 文件并按要求统计
with open('./data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') 
    count1 = count2 = count3 = 0
    for row in csv_reader:
        title = row[1]
        # 1.统计包含python或Python行数
        if "python" in title or "Python" in title:
            count1 += 1
        # 2.统计包含JavaScript, javascript or Javascript行数
        if "JavaScript" in title or "javascript" in title or "Javascript" in title:
            count2 += 1
        # 3.统计包含Java但不包含JavaScript的行数
        if "java" in title and "JavaScript" not in title:
            count3 += 1
    print(count1, count2, count3)