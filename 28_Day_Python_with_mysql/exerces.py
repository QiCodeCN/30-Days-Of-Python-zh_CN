import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qicode",
  database="thirty_days_of_python"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE students (id int AUTO_INCREMENT PRIMARY KEY, name varchar(100), country varchar(20), city varchar(20), age int)")
# sql = "INSERT INTO students (name, country, city, age) VALUES (%s, %s, %s, %s)"
# val = ("MegaQi", "China", "ShangHai", 36)
# mycursor.execute(sql, val)

# sql = "INSERT INTO students (name, country, city, age) VALUES (%s, %s, %s, %s)"
# val = [
#   ('David', 'UK', 'London', 30),
#   ('John', 'Sweden', 'Stockholm', 22)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# # 更新操作
# sql = "DELETE FROM students WHERE id = 1"
# mycursor.execute(sql)
# mydb.commit()

# 查询看是否更新成功
# mycursor.execute("SELECT * FROM students")
# results = myresult = mycursor.fetchall()
# print(results)

try:
  mydb.start_transaction()

  sql = "INSERT INTO students (name, country, city, age) VALUES (%s, %s, %s, %s)"
  val = ("李雷", "中国", "北京", 30)
  mycursor.execute(sql, val)

  sql_update = "UPDATE students SET age = 18 WHERE name = '李雷'"
  mycursor.execute(sql_update)

  mydb.commit()

except:
  mydb.rollback()