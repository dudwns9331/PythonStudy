# 오늘의 날짜는?

"""
2020-12-29-16 오전 11:14
안영준

지금 시각을 UTC+0(세계 표준시)을 기준으로 나타냈을 때의 연도, 월, 일을 한 줄에 하나씩 순서대로 출력한다.

"""

import datetime

a = str(datetime.date.today()).split('-')
for i in range(a.__len__()):
    print(a.__getitem__(i))
