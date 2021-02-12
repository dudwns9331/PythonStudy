# N번째 큰 수

"""
2021-02-12 오후 12:15
안영준

문제 : https://www.acmicpc.net/problem/2693

"""

T = int(input())

for i in range(T):
    result = list(map(int, input().split()))
    result.sort()
    print(result[-3])
