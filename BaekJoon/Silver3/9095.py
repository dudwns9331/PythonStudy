# 1, 2, 3 더하기

"""
2021-04-04 오후 2:56
안영준

문제 : https://www.acmicpc.net/problem/9095
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

number = list()

for i in range(eval(input())):
    number.append(eval(input()))

dp = [1, 2, 4]

for k in range(3, max(number)):
    dp.append(dp[k - 1] + dp[k - 2] + dp[k - 3])

for j in number:
    print(dp.__getitem__(j - 1))
