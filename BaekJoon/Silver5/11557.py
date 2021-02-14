# Yangjojang of The Year

"""
2021-02-14 오후 3:28
안영준

문제 : https://www.acmicpc.net/problem/11557

"""

T = int(input())

result = list()

for i in range(T):
    for _ in range(int(input())):
        a, b = map(str, input().split())
        result.append((a, int(b)))
    print(max(result, key=lambda x: x[1])[0])
