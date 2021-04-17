# N 과 M (5)

"""
2021-04-16 오후 9:42
안영준

문제 : https://www.acmicpc.net/problem/15654
"""
import sys

from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))

perm = permutations(number, M)

result = list(perm)
result.sort()

for i in result:
    print(' '.join(map(str, i)))
