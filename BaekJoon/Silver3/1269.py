# 대칭 차집합

"""
2021-05-30 오후 2:14
안영준

문제 : https://www.acmicpc.net/problem/1269
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A.difference(B)) + len(B.difference(A)))
