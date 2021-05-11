# N 과 M

"""
2021-05-11 오후 4:32
안영준

문제 : https://www.acmicpc.net/problem/15651
"""
import sys

from itertools import product as pd

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = [i for i in range(1, N + 1)]

for num in pd(number, repeat=M):
    for i in num:
        print(i, end=' ')
    print()
