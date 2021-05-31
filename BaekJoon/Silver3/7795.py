# 먹을 것인가 먹힐 것인가

"""
2021-05-30 오후 12:57
안영준

문제 : https://www.acmicpc.net/problem/7795
"""

import bisect
import sys

input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    count = 0

    for j in A:
        count += (bisect.bisect(B, j - 1))
    print(count)
