# 헬멧과 조끼

"""
2021-02-10 오전 1:41
안영준

문제 : https://www.acmicpc.net/problem/15781

"""

N, M = map(int, input().split())

h = list(map(int, input().split()))
j = list(map(int, input().split()))

print(max(h) + max(j))
