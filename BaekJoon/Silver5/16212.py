# 정열적인 정렬

"""
2021-02-16 오전 12:42
안영준

문제 : https://www.acmicpc.net/problem/16212

"""

n = int(input())

result = list(map(int, input().split()))

result.sort()

print(' '.join(map(str, result)))
