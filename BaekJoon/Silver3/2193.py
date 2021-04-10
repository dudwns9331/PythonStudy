# 이친수

"""
2021-04-10 오후 3:55
안영준

문제 : https://www.acmicpc.net/problem/2193
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N = eval(input())

dp = [1, 1]

for i in range(2, N):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp.pop())
