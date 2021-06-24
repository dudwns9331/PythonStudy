# 가장 큰 증가 부분 수열

"""
2021-06-24 오후 2:46
안영준

문제 : https://www.acmicpc.net/problem/11055
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
number = list(map(int, input().split()))
dp = [0 for i in range(N)]
dp[0] = number[0]
for i in range(1, N):
    temp = []
    for j in range(i - 1, -1, -1):
        if number[i] > number[j]:
            temp.append(dp[j])
    if not temp:
        dp[i] = number
    else:
        dp[i] = number[i] + max(temp)
print(max(dp))
