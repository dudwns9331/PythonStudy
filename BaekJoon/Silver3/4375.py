# 1

"""
2021-05-17 오후 9:14
안영준

문제 : https://www.acmicpc.net/problem/4375
"""

import sys

input = lambda: sys.stdin.readline().rstrip()
try:
    while True:
        N = input()
        result = "1" * len(N)
        while int(result) % int(N):
            result += "1"
        print(len(result))
except:
    pass
