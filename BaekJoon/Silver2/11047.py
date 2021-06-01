# 동전 0

"""
2021-05-31 오후 8:34
안영준

문제 : https://www.acmicpc.net/problem/11047
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

coin = []
result = 0
for i in range(N):
    coin.append(int(input()))
for i in range(N - 1, -1, -1):
    if K == 0:
        break
    if coin[i] > K:
        continue
    result += K // coin[i]
    K %= coin[i]
print(result)
