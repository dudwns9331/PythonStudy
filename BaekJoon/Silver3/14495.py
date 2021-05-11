# 피보나치 비스무리한 수열

"""
2021-05-11 오후 4:38
안영준

문제 : https://www.acmicpc.net/problem/14495
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

dp = [1, 1, 1]

for i in range(3, eval(input())):
    dp.append(dp[i - 1] + dp[i - 3])

print(dp[-1])
