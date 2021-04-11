# 파도반 수열

"""
2021-04-11 오후 7:08
안영준

문제 : https://www.acmicpc.net/problem/9461
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

dp = [1, 1, 1]

result = list()
number = list()

for i in range(eval(input())):
    number.append(eval(input()))

for j in range(3, max(number)):
    dp.append(dp[j - 2] + dp[j - 3])

for k in number:
    print(dp[k - 1])
