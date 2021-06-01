# N과 M (10)

"""
2021-05-30 오후 2:29
안영준

문제 : https://www.acmicpc.net/problem/15664
"""
import itertools
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))

number.sort()

comb = itertools.combinations(number, M)

result = set(comb)
result = sorted(list(result))

for i in result:
    print(' '.join(map(str, i)))
