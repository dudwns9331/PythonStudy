# 문자열

"""
2021-03-17 오후 5:35
안영준

문제 : https://www.acmicpc.net/problem/1120
"""

A, B = list(input().split())
minimum = 50

for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            count += 1

    if count < minimum:
        minimum = count
print(minimum)
