# 패션왕 신해빈

"""
2021-05-06 오전 12:19
안영준

문제 : https://www.acmicpc.net/problem/9375
"""

# (옷의 종류 + 1) * (옷의 종류 + 1) * ... - 1 => result


from collections import Counter
from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())
for i in range(T):
    N = int(input())
    string = []
    for j in range(N):
        c, var = input().split()
        string.append(var)
    result = Counter(string)
    number = 1

    for key in result:
        number *= result[key] + 1
    print(number - 1)
