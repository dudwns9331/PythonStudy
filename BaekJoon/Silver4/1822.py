# 차집합

"""
2021-03-26 오전 12:44
안영준

문제 : https://www.acmicpc.net/problem/1822
"""

import sys

input = lambda: sys.stdin.readline()

A, B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

length = len(A_set)

A_set.difference_update(B_set)

A_set = sorted(list(A_set))

if len(A_set) == 0:
    print(0)
else:
    print(len(A_set))
    print(' '.join(map(str, A_set)))
