# 로프

"""
2021-03-09 오후 4:24
안영준

문제 : https://www.acmicpc.net/problem/2217

"""

N = int(input())

rope = list()
result = list()

for i in range(N):
    rope.append(int(input()))

rope = sorted(rope, reverse=True)

for i in range(N):
    result.append(rope[i] * (i + 1))

print(max(result))
