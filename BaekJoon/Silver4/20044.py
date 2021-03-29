# Project Teams

"""
2021-03-29 오전 9:13
안영준

문제 : https://www.acmicpc.net/problem/20044
"""

import sys

input = lambda: sys.stdin.readline()

N = int(input())
number = list(map(int, input().split()))

number.sort()
result = list()

for i in range(len(number) // 2):
    result.append(number[i] + number[-i - 1])

print(min(result))
