# 소인수분해

"""
2021-03-08 오전 10:34
안영준

문제 : https://www.acmicpc.net/problem/11653

"""

N = int(input())

for i in range(2, N + 1):
    while N % i == 0:
        N /= i
        print(i)
    