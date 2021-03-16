# LCM

"""
2021-03-15 오후 9:04
안영준

문제 : https://www.acmicpc.net/problem/5347

"""

import math

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
