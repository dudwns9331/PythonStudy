# 소수

"""
2021-02-26 오전 11:14
안영준

문제 : https://www.acmicpc.net/problem/2581

"""

N = int(input())

M = int(input())

result_count = 0
result = list()

for i in range(N, M + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        result.append(i)

if len(result) == 0:
    print('-1')
else:
    print(sum(result))
    print(min(result))
