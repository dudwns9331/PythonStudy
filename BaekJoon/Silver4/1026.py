# 보물

"""
2021-02-27 오후 12:47
안영준

문제 : https://www.acmicpc.net/problem/1026

"""

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

result = list()

for i in range(len(A)):
    result.append(A[i] * B[i])

print(sum(result))
