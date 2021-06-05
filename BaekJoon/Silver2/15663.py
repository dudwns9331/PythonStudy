# N 과 M 9

"""
2021-06-06 오전 1:23
안영준

문제 : https://www.acmicpc.net/problem/15663
"""

import itertools
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))

number.sort()

comb = itertools.permutations(number, M)
result = sorted(list(set(comb)))

for i in result:
    print(' '.join(map(str, i)))
