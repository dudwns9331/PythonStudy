# 주몽

"""
2021-03-25 오후 7:32
안영준

문제 : https://www.acmicpc.net/problem/1940
"""

import sys

input = lambda: sys.stdin.readline()

N = int(input())
M = int(input())

materials = list(map(int, input().split()))

materials.sort()

count = 0

i, j = 0, N - 1

while i < j:
    if materials[i] + materials[j] == M:
        count += 1
        i += 1
        j -= 1
    elif materials[i] + materials[j] < M:
        i += 1
    else:
        j -= 1
        
print(count)
