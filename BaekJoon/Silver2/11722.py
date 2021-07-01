# 가장 긴 감소하는 부분 수열

"""
2021-07-01 오후 7:42
안영준

문제 : https://www.acmicpc.net/problem/11722
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

sequence = list(map(int, input().split()))

dp = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if sequence[i] < sequence[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
