# 수 이어 쓰기 1

"""
2021-05-01 오후 2:29
안영준

문제 : https://www.acmicpc.net/problem/1748
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N = input()
length = len(N) - 1
result = 0
i = 0

while i < length:
    result += 9 * (10 ** i) * (i + 1)
    i += 1

result += ((int(N) - (10 ** length)) + 1) * (length + 1)

print(result)
