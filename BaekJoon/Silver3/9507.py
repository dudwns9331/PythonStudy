# Generation of Tribbles

"""
2021-05-06 오전 9:36
안영준

문제 : https://www.acmicpc.net/problem/9507
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for i in range(t):
    dp = [1, 1, 2, 4]
    n = int(input())
    for j in range(4, n + 1):
        dp.append(dp[j - 1] + dp[j - 2] + dp[j - 3] + dp[j - 4])
    print(dp[n])
