# 나무조각

"""
2021-02-14 오후 12:20
안영준

문제 : https://www.acmicpc.net/problem/2947

"""

result = list(map(int, input().split()))

for i in range(len(result)):
    for j in range(1, len(result)):
        if result[j] < result[j - 1]:
            result[j], result[j - 1] = result[j - 1], result[j]
            print(' '.join(map(str, result)))
