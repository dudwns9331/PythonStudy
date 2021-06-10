# 차이를 최대로

"""
2021-06-10 오후 8:21
안영준

문제 : https://www.acmicpc.net/problem/10819
"""

import sys

from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

number = list(map(int, input().split()))

perm = list(permutations(number, N))

result = 0

for i in perm:
    number_list = list(i)
    temp = 0
    for j in range(1, N):
        temp += abs(number_list[j] - number_list[j - 1])
    result = max(result, temp)

print(result)
