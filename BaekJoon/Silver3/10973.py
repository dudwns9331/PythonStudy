# 이전 순열

"""
2021-05-09 오후 3:46
안영준

문제 : https://www.acmicpc.net/problem/10973
"""

import sys

from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

number = list(map(int, input().split()))

perm = permutations(number, N)

result = list(perm)

result.sort()

if result.index(tuple(number)) == 0:
    print(-1)
else:
    print(*result[result.index(tuple(number)) - 1])
