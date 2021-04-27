# N 과 M (8)

"""
2021-04-27 오후 6:23
안영준

문제 : https://www.acmicpc.net/problem/15657
"""
import sys

from itertools import combinations_with_replacement

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))

number.sort()

comb = combinations_with_replacement(number, M)

result = list(comb)

result.sort()

for i in result:
    print(' '.join(map(str, i)))
