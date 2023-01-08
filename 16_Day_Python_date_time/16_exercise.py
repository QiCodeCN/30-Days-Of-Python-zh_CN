# 1.使用 datetime 模块分别获取年、月、日、时、分 和 时间戳信息
from datetime import datetime
today = datetime.now()
print('今年是：',today.year)
print('当前月：', today.month)
print('今天是', today.year)
print('当前时间', f'{today.hour}:{today.minute}:{today.second}')

# 2. 使用 `%m/%d/%Y, %H:%M:%S` 格式输出当前时间
format_date = datetime.strftime(today, '%m/%d/%Y, %H:%M:%S')
print('格式化的时间为：',format_date)

# 3. 如果时间是 “2023年1月1日”，将此字符串时间转成时间类型
pdate = datetime.strptime('2023年1月1日', '%Y年%m月%d日')
print("字符时间转日期：", pdate)

# 4. 计算当前时间和元旦那天的时间差
from datetime import date
new_year_day = date(year=2023, month=1, day=1)
print('当前距离元旦已经过:', date.today() - new_year_day,"天")

# 5. 计算当前时间距离1970年1月1的时间差或时间戳
# 方法一和第4题一样处理
# 方法二使用 time 计算时间戳
import time
print("时间戳", time.time())

# 6. 思考题：想想这个 datetime 模块可以实际应用在那些编码场景中呢？
# 略..