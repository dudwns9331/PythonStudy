# 덩치

"""
2021-02-13 오후 10:57
안영준

문제 : https://www.acmicpc.net/problem/7568

"""

person = []

for i in range(int(input())):
    a, b = map(int, input().split())
    person.append((a, b))

for j in person:
    count = 1
    for k in person:
        if j[0] < k[0] and j[1] < k[1]:
            count += 1
    print(count, end=' ')
