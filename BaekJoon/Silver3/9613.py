# GCD 합

"""
2021-04-19 오후 11:59
안영준

문제 : https://www.acmicpc.net/problem/9613
"""

import math
import sys
from itertools import combinations


def gcd(a, b):
    return gcd(b, a % b) if b else a


input = lambda: sys.stdin.readline().rstrip()

for i in range(eval(input())):
    number = list(map(int, input().split()))
    number = number[1:]
    gcd_number = list(combinations(number, 2))
    result = 0
    for j in gcd_number:
        result += math.gcd(j[0], j[1])
    print(result)
