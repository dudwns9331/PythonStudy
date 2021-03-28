# 악수

"""
2021-03-27 오후 6:23
안영준

문제 : https://www.acmicpc.net/problem/8394
"""

n = int(input())
a, b = 1, 0
for i in range(n):
    a, b = (a + b) % 10, a % 10
print(a)
