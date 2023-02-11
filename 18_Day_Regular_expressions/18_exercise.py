import re

# 1.1 下面这段话中出现频率最高的单词是什么
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\w+', paragraph)  # 通过正则提取所有单词

word_dict = dict()  # 通过字典统计
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

word_tuple = [(v, k) for k,v in word_dict.items()]  #转元组list
word_sort = sorted(word_tuple, reverse=True)  # 内置排序
print(word_sort)


# 1.2 提取对话中x轴点数字并计算最远点距离
conents = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
points = re.findall("[-]*\d+", conents)
print("points=", points)
change_to_int = [int(i) for i in points]
sorted_points = sorted(change_to_int)
print("sorted_points=", sorted_points)

distance = abs(sorted_points[0]) + abs(sorted_points[-1])
print("distance=", distance)


# 2.1 编写一个方法来识别字符串是否是有效的python变量
# 关于合法python变量名的定义如果忘记请回看day2内容
def is_valid_variable(name):
    if re.match(r"^[^0-9][a-zA-Z0-9_]+$", name) is None:
        return False
    else:
        return True

print("Name 字符是否符合变量命名规则：", is_valid_variable("Name"))
print("_Test字符是否符合变量命名规则：", is_valid_variable("_Test"))
print("Number8899  字符是否符合变量命名规则：", is_valid_variable("Number8899"))
print("char$% 字符是否符合变量命名规则：", is_valid_variable("char$%123"))
print("98abc 字符是否符合变量命名规则：", is_valid_variable("98abc"))

# 3.1 清除以下文本无用的字符。且统计出优化后的文本中出现频率最高的三个单词。
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(sentence):
    split_blank = re.findall("[^ ]+", sentence)
    word_list = []
    for chars in split_blank:
        word = re.sub("\W+", '', chars)
        word_list.append(word)
    return " ".join(word_list)

def most_frequent_words(clean_text):
    # 统计处理方法参考练习1.1，需要注意的此函数最终只需要返回排序后前三个单词
    # 这里给出围绕本章节知识点另外一种解法供参考，当然方法肯定还有很多，
    # 尝试你的思路(不限制正则)，看看能不能有更多更好的办法呢？
    split_word = re.findall("\w+", cleaned_text)
    unique_word = list(set(split_word))
    top_one = top_two = top_three = ('', 0)
    for uword in unique_word:
        find_word = re.findall(uword, clean_text)
        word_count = len(find_word)
        if word_count > top_one[1]:
            top_three = top_two
            top_two = top_one
            top_one = (uword, word_count)
        elif word_count > top_two[1]:
            top_three = top_two
            top_two = (uword, word_count)
        elif word_count > top_three[1]:
            top_three = (uword, word_count)
        else:
            pass
    return [top_one, top_two, top_three]
    

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text)) # 因题目中可能存在多个相同排第三的所以结果每次运行结果会变
