# 게임을 만든 동준이

"""
2021-03-24 오후 12:20
안영준

문제 : https://www.acmicpc.net/problem/2847
"""

import sys

input = lambda: sys.stdin.readline()

N = int(input())

result = list()

for i in range(N):
    result.append(int(input()))

count = 0

for j in range(len(result) - 1, 0, -1):
    if result[j] <= result[j - 1]:
        count += result[j - 1] - result[j] + 1
        result[j - 1] = result[j] - 1

print(count)
