# N 과 M 11

"""
2021-06-05 오후 8:45
안영준

문제 : https://www.acmicpc.net/problem/15665
"""

import sys
from itertools import product

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

number = list(map(int, input().split()))
number.sort()
number = list(product(number, repeat=M))

number = sorted(list(set(number)))

for i in number:
    print(*i)
