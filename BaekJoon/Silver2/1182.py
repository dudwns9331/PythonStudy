# 부분 수열의 합

"""
2021-06-23 오후 8:34
안영준

문제 : https://www.acmicpc.net/problem/1182
"""
import itertools
import sys

N, S = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(1, N + 1):
    sequence = list(itertools.combinations(numbers, i))
    for j in sequence:
        if sum(j) == S:
            count += 1

print(count)
