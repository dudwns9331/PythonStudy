# 하노이 탑 이동 순서

"""
2021-06-18 오전 8:56
안영준

문제 : https://www.acmicpc.net/problem/11729
"""

import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())


def hanoi(N, start, to, temp):
    if N == 1:
        print(start, temp)
    else:
        hanoi(N - 1, start, temp, to)
        # start에서 temp로
        print(start, temp)
        hanoi(N - 1, to, start, temp)


result = 1
for i in range(n - 1):
    result = result * 2 + 1
print(result)
hanoi(n, 1, 2, 3)
