# 백대일

"""
2021-03-04 오전 8:56
안영준

문제 : https://www.acmicpc.net/problem/14490

"""

import math

string = input().split(':')

a = int(string[0])
b = int(string[1])

gcd = math.gcd(a, b)

a = a // gcd
b = b // gcd

print(f'{a}:{b}')
