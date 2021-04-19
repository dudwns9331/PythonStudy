# 모든 순열

"""
2021-04-19 오후 3:29
안영준

문제 : https://www.acmicpc.net/problem/10974
"""
import sys

from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
number = [i for i in range(1, N + 1)]

perm = permutations(number, N)

result = list(perm)

for i in result:
    print(' '.join(map(str, i)))
