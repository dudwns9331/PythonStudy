# 숫자 빈도수

"""
2021-02-16 오전 12:56
안영준

문제 : https://www.acmicpc.net/problem/14912

"""

n, d = map(int, input().split())

count = 0
for i in range(1, n + 1):
    count += str(i).count(str(d))
print(count)
