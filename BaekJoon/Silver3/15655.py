# N 과 M 6

"""
2021-04-22 오후 11:38
안영준

문제 : https://www.acmicpc.net/problem/15655
"""
import sys

from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))

number.sort()

comb = combinations(number, M)

result = list(comb)

for i in result:
    print(' '.join(map(str, i)))
