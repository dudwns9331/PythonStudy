# 국영수

"""
2021-03-11 오후 5:10
안영준

문제 : https://www.acmicpc.net/problem/10825

"""
import sys

input = lambda: sys.stdin.readline()

N = int(input())
result = list()

for i in range(N):
    result.append(list(input().split()))

result.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in result:
    print(j[0])
