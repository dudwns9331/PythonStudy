# 문자열 집합

"""
2021-05-30 오전 12:15
안영준

문제 : https://www.acmicpc.net/problem/14425
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

strings = list()
count = 0

for i in range(N):
    strings.append(input())

for j in range(M):
    if input() in strings:
        count += 1

print(count)
