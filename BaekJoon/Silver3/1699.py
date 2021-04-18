# 제곱수의 합

"""
2021-04-18 오후 2:22
안영준

문제 : https://www.acmicpc.net/problem/1699
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

number = int(input())
result_array = [0] * (number + 1)

for i in range(1, number + 1):
    result_array[i] = i
    for j in range(1, i):
        if (j * j) > i:
            break
        result_array[i] = min(result_array[i], result_array[i - j * j] + 1)
print(result_array[number])
