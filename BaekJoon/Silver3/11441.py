# 합 구하기

"""
2021-05-27 오전 9:50
안영준

문제 : https://www.acmicpc.net/problem/11441
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

numbers = list(map(int, input().split()))
#
# M = int(input())
#
# for _ in range(M):
#     i, j = map(int, input().split())
#     print(sum(numbers[i - 1:j]))

prefix_sum = [numbers[0]]

for i in range(1, N):
    prefix_sum.append(prefix_sum[-1] + numbers[i])

M = int(input())

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(prefix_sum[j - 1])
    else:
        print(prefix_sum[j - 1] - prefix_sum[i - 2])
