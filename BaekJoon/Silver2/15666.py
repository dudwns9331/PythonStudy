# N 과 M 12

"""
2021-06-07 오전 12:22
안영준

문제 : https://www.acmicpc.net/problem/15666
"""

import itertools
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))

number = set(number)
number = list(number)

number.sort()

comb = itertools.combinations_with_replacement(number, M)

result = sorted(list(comb))

for i in result:
    print(' '.join(map(str, i)))
