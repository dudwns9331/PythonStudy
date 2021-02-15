# 0의 개수

"""
2021-02-16 오전 12:40
안영준

문제 : https://www.acmicpc.net/problem/11170

"""

for i in range(int(input())):
    count = 0
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        count += str(j).count('0')
    print(count)
