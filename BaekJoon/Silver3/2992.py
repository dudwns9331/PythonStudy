# 크면서 작은 수

"""
2021-05-29 오후 11:55
안영준

문제 : https://www.acmicpc.net/problem/2992
"""

import itertools
import sys

input = lambda: sys.stdin.readline().rstrip()

N = input()

result_list = set(itertools.permutations(N, len(N)))

result_list = list(result_list)

result_list.sort()

# print(result_list)

result = list()

for i in result_list:
    result.append(int(''.join(map(str, i))))

# print(result)

if result.index(int(N)) + 1 == len(result):
    print(0)
else:
    print(result[result.index(int(N)) + 1])
