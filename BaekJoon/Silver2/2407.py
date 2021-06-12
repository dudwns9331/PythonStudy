# 조합

"""
2021-06-12 오후 10:32
안영준

문제 : https://www.acmicpc.net/problem/2407
"""

import sys
from math import comb

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

print(comb(N, M))
