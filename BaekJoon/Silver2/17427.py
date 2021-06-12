# 약수들의 합 2

"""
2021-06-12 오후 10:03
안영준

문제 : https://www.acmicpc.net/problem/17427
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

result = 0
for i in range(1, N + 1):
    result += (N // i) * i

print(result)
