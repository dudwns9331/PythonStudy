# 최소공배수

"""
2021-05-13 오전 11:48
안영준

문제 : https://www.acmicpc.net/problem/13241

"""

import math

a, b = map(int, input().split())

print(a * b // math.gcd(a, b))
