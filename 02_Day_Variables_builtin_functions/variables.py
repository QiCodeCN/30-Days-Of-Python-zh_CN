
# Python变量

first_name = 'Mega'
last_name = 'Qi'
country = 'China'
city = 'ShangHai'
age = 200
is_married = True
skills = ['HTML', 'JS', 'JAVA', 'React', 'Python']
person_info = {
   'name':'大奇',
   'country':'中国',
   'city':'上海'
   }

# 打印存储在变量中的值

print('First name:', first_name)
print('First name length:', len(first_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# 在一行中声明多个变量

name, country, age = 'MegaQi', 'China', 18

print(name, country, age)
print('Nick Name:', name)
print('Country: ', country)
print('Age: ', age)