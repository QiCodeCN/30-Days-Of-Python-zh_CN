# 1.写一个数据计算类，通过各类方法实现数学计算

import statistics
import numpy
 
class Statistics:
    def __init__(self, ages=[]):
      self.ages = ages

    def count(self):
       return len(self.ages)

    def sum(self):
       sum = 0
       for age in self.ages:
          sum = sum + age
       return sum

    def min(self):
       min = self.ages[0]
       for i in range(1, len(self.ages)):
          if self.ages[i] < min:
             min = self.ages[i]
       else:
          pass
       return min
    
    def max(self):
       max = self.ages[0]
       for i in range(1, len(self.ages)):
          if self.ages[i] > max:
             max = self.ages[i]
       else:
          pass
       return max
    
    def mean(self):
       return statistics.mean(self.ages)
    
    def median(self):
       return statistics.median(self.ages)
    
    def mode(self):
       return statistics.mode(self.ages)
    
    def std(self):
       return numpy.std(self.ages)
    
    def var(self):
       return numpy.var(self.ages)
           

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5


# 2.实现 PersonAccount 类和方法计算相关收入，花销和结余
class PersonAccount:
   def __init__(self, name, incomes=[], expenses=[]):
      self.name = name
      self.incomes = incomes
      self.expenses = expenses

   def total_income(self):
      total = 0
      for income in self.incomes:
         total = total + income
      return total

   def total_expense(self):
      total = 0
      for expense in self.expenses:
         total = total + expense
      return total

   def account_info(self):
      return f"{self.name}的总收入为{self.total_income()}, 总支出为{self.total_expense()}"

   def add_income(self, income):
      self.incomes.append(income)

   def add_expense(self, expense):
      self.expenses.append(expense)

   def account_balance(self):
      return self.total_income() - self.total_expense()
   
pa = PersonAccount(name="MeagaQi", incomes=[100,200,300,500], expenses=[30,40,20,10])
print("初始进账：",pa.total_income())
print("初始出账：",pa.total_expense())
print("我的当前账户：",pa.account_info())
print("增加一份输入120元")
print("我又花出去了20元")
pa.add_income(120)
pa.add_expense(20)
print("当前结余",pa.account_balance())