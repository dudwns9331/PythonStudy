# 상근이의 여행

"""
2021-05-05 오후 2:09
안영준

문제 : https://www.acmicpc.net/problem/9372
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    plane = set()
    result = {i for i in range(1, N + 1)}
    count = 0
    for j in range(M):
        a, b = map(int, input().split())
        plane.add(a)
        plane.add(b)
        if plane != result:
            count += 1
        else:
            continue
    print(count + 1)
