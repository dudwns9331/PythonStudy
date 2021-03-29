# 터렛

"""
2021-03-29 오전 10:05
안영준

문제 : https://www.acmicpc.net/problem/1002
"""

import sys

input = lambda: sys.stdin.readline()

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    R = [r1, r2, r]
    m = max(R)
    R.remove(m)

    if r == 0 and r1 == r2:
        print(-1)
    elif m > sum(R):
        print(0)
    elif r == r1 + r2 or m == sum(R):
        print(1)
    else:
        print(2)
