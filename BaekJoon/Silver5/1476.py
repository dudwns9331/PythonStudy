# 날짜 계산

"""
2021-02-22 오후 7:53
안영준

문제 : https://www.acmicpc.net/problem/1476

블로그 참조함

"""

E, S, M = map(int, input().split())
year = 1

while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1
