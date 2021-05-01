# 링

"""
2021-05-01 오후 2:13
안영준

문제 : https://www.acmicpc.net/problem/3036
"""

import math
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
circle = list(map(int, input().split()))

first = circle[0]

for i in range(1, N):
    var = math.gcd(first, circle[i])
    if var != 1:
        result = str(first // var) + "/" + str(circle[i] // var)
    else:
        result = str(first) + "/" + str(circle[i])
    print(result)
