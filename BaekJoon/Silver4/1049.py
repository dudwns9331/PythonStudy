# 기타줄

"""
2021-03-18 오전 9:16
안영준

문제 : https://www.acmicpc.net/problem/1049
"""

# 끊어진 기타줄의 개수 N
# 기타줄 브랜드 M

# 6개 패키지의 가격, 낱개의 가격

import sys

input = lambda: sys.stdin.readline()

N, M = map(int, input().split())

result = list()

for i in range(M):
    result.append(list(map(int, input().split())))

result.sort(key=lambda x: x[0])
min_set = result[0][0]
result.sort(key=lambda x: x[1])
min_piece = result[0][1]

Q = N // 6
R = N % 6

min_price = list()

min_price.append((Q + 1) * min_set)
min_price.append(min_piece * N)
min_price.append(Q * min_set + R * min_piece)

print(min(min_price))
