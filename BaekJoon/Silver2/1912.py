# 연속합

"""
2021-06-08 오전 10:04
안영준

문제 : https://www.acmicpc.net/problem/1912
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
sequence = list(map(int, input().split()))
result = [sequence[0]]

for i in range(len(sequence) - 1):
    result.append(max(result[i] + sequence[i + 1], sequence[i + 1]))
print(max(result))
