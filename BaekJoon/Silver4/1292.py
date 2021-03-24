# 쉽게 푸는 문제

"""
2021-03-23 오후 5:13
안영준

문제 : https://www.acmicpc.net/problem/1292
"""

import sys

input = lambda: sys.stdin.readline()

start, end = map(int, input().split())

sequence = list()
result = list()

for i in range(1, 1001):
    for j in range(i):
        sequence.append(i)

print(sum(sequence[start - 1: end]))
