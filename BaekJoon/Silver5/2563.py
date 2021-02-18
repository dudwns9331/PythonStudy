# 색종이

"""
2021-02-19 오전 1:32
안영준

문제 : https://www.acmicpc.net/problem/2563

"""

N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

answer = 0

for k in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

for row in paper:
    answer += row.count(1)
print(answer)
