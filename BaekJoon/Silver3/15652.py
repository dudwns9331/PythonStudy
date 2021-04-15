# N 과 M 3

"""
2021-04-14 오후 1:27
안영준

문제 : https://www.acmicpc.net/problem/15652
"""
import sys

from itertools import combinations_with_replacement

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = [i for i in range(1, N + 1)]

comb = combinations_with_replacement(number, M)

result = list(comb)

for i in result:
    print(' '.join(map(str, i)))
