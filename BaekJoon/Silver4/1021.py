# 회전하는 큐

"""
2021-03-11 오전 12:11
안영준

문제 : https://www.acmicpc.net/problem/1021

"""

import sys

N, M = map(int, (sys.stdin.readline()).split())

a = list()
b = list()
for i in range(N + M):
    if i < N:
        a.append(sys.stdin.readline().rstrip())
    if i >= N:
        b.append(sys.stdin.readline().rstrip())

result = sorted(list(set(a) & set(b)))
print(len(result))
print('\n'.join(map(str, result)))
