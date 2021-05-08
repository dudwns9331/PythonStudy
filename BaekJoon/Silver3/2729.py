# 이진수 덧셈

"""
2021-05-07 오전 9:12
안영준

문제 : https://www.acmicpc.net/problem/2729
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    bin_a = int(str(a), 2)
    bin_b = int(str(b), 2)
    print(format(bin_a + bin_b, 'b'))
