# 구간합 구하기 4

"""
2021-04-26 오전 9:32
안영준

문제 : https://www.acmicpc.net/problem/11659
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
number = list(map(int, input().split()))
result = [0 for _ in range(N)]
result[0] = number[0]
for i in range(1, N):
    result[i] = result[i - 1] + number[i]

for _ in range(M):
    a, b = map(int, input().split())
    answer = result[b - 1] - result[a - 1] + number[a - 1]
    print(answer)
