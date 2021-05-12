# N과 M 7

"""
2021-05-02 오후 2:28
안영준

문제 : https://www.acmicpc.net/problem/15656
"""
import sys

from itertools import product as pd

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))

number.sort()

for num in pd(number, repeat=M):
    for i in num:
        print(i, end=' ')
    print()
