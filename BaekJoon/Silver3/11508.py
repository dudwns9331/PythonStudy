# 2+1 세일

"""
2021-05-30 오후 2:20
안영준

문제 : https://www.acmicpc.net/problem/11508
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

item = list()

for i in range(int(input())):
    item.append(int(input()))

item.sort(reverse=True)

result = 0

for i in range(len(item)):
    if i % 3 == 2:
        continue
    else:
        result += item[i]

print(result)
