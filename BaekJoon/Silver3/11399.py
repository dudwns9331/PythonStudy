# ATM

"""
2021-04-06 오후 5:02
안영준

문제 : https://www.acmicpc.net/problem/11399
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N = eval(input())

p_list = list(map(int, input().split()))
p_list.sort()

result = list()

for i in range(len(p_list)):
    result.append(sum(p_list[:i]) + p_list[i])

print(sum(result))
