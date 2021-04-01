# 교수가 된 현우

"""
2021-03-31 오전 10:51
안영준

문제 : https://www.acmicpc.net/problem/3474
"""

import sys

input = lambda: sys.stdin.readline()

for _ in range(eval(input())):
    n = eval(input())
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    print(count)
