# 순서쌍의 곱의 합

"""
2021-03-25 오후 7:46
안영준

문제 : https://www.acmicpc.net/problem/13900
"""

import sys

input = lambda: sys.stdin.readline()

N = int(input())
number = list(map(int, input().split()))
sum_number = sum(number)
result = 0
for i in number:
    sum_number -= i
    result += i * sum_number
print(result)
