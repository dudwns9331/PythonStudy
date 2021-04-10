# 바이러스

"""
2021-04-09 오후 4:30
안영준

문제 : https://www.acmicpc.net/problem/2606
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t = int(input())

result = [[0] * n for i in range(n)]
visit = [0 for i in range(n)]

for i in range(t):
    a, b = map(int, input().split())
    result[a - 1][b - 1] = 1
    result[b - 1][a - 1] = 1


def dfs(v):
    visit[v] = 1
    for i in range(n):
        if result[v][i] == 1 and visit[i] == 0:
            dfs(i)


dfs(0)
count = 0
for i in range(1, n):
    if visit[i] == 1:
        count += 1
print(count)
