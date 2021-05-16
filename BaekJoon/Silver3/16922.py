# 로마숫자 만들기

"""
2021-05-16 오후 8:57
안영준

문제 : https://www.acmicpc.net/problem/16922
"""

import sys

from itertools import combinations_with_replacement

input = lambda: sys.stdin.readline().rstrip()

number = [1, 5, 10, 50]
N = int(input())
result = []
for i in combinations_with_replacement(range(4), N):
    num_sum = 0
    for j in i:
        num_sum += number[j]
    if num_sum not in result:
        result.append(num_sum)
print(len(result))
