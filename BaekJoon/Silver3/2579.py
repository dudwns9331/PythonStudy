# 계단 오르기

"""
2021-04-08 오전 8:57
안영준

문제 : https://www.acmicpc.net/problem/2579
"""

import sys

input = lambda: sys.stdin.readline().rstrip()
number = list()
dp = []

N = eval(input())

for _ in range(N):
    number.append(eval(input()))

dp.append(number[0])
dp.append(max(number[0] + number[1], number[1]))
dp.append(max(number[0] + number[2], number[1] + number[2]))

for i in range(3, N):
    dp.append(max(dp[i - 2] + number[i], dp[i - 3] + number[i] + number[i - 1]))
    
print(dp.pop())
