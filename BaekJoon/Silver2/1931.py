# 회의실 배정

"""
2021-06-17 오후 3:28
안영준

문제 : https://www.acmicpc.net/problem/1931
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
time = [[0] * 2 for _ in range(N)]
for i in range(N):
    s, e = map(int, input().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]
print(cnt)
