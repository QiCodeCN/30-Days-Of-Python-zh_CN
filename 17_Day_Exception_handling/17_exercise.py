# 1. 解压缩前五个国家并将它们存储在一个变量 nordic_nations 中，将Estonia和Russia分别存储在es和ru中
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_nations, es, ru = names
print("nordic:", nordic_nations)
print("es:", es)
print("ru:", ru)