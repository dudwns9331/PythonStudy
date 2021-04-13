# N 과 M 2

"""
2021-04-13 오전 8:59
안영준

문제 : https://www.acmicpc.net/problem/15650
"""

import sys

from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = [i for i in range(1, N + 1)]

comb = combinations(number, M)

result = list(comb)

for i in result:
    print(' '.join(map(str, i)))
