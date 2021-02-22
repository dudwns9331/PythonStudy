# 소수 찾기

"""
2021-02-22 오후 3:29
안영준

문제 : https://www.acmicpc.net/problem/1978

"""

N = int(input())

number = list(map(int, input().split()))

result_count = 0

for i in range(len(number)):
    count = 0
    for j in range(1, number[i] + 1):
        if number[i] % j == 0:
            count += 1
    if count == 2:
        result_count += 1
print(result_count)
