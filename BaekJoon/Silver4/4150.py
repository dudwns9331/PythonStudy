# 피보나치 수

"""
2021-03-26 오전 9:07
안영준

문제 : https://www.acmicpc.net/problem/4150
"""

import sys as system

input = lambda: system.stdin.readline()

N = int(input())

f0 = 0
f1 = 1
fi = 0

for i in range(N):
    fi = f0
    f0 = f1
    f1 = fi + f1
print(f0)
