# N 과 M

"""
2021-04-11 오후 7:21
안영준

문제 : https://www.acmicpc.net/problem/15649
"""

import sys

from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = [i for i in range(1, N + 1)]

perm = permutations(number, M)

result = list(perm)

for i in result:
    print(' '.join(map(str, i)))
