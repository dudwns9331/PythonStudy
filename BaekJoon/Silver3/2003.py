# 수들의 합2

"""
2021-04-29 오전 9:39
안영준

문제 : https://www.acmicpc.net/problem/2003
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

result = list(map(int, input().split()))

count = 0

for i in range(N):
    temp = 0
    for j in range(i, N):
        temp += result[j]
        if temp == M:
            count += 1
            break
        elif temp > M:
            break
print(count)
