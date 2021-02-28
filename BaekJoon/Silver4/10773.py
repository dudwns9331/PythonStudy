# 제로

"""
2021-02-28 오후 12:47
안영준

문제 : https://www.acmicpc.net/problem/10773

"""

result = list()

for i in range(int(input())):
    n = int(input())
    if n == 0:
        result.pop()
    else:
        result.append(n)

print(sum(result))
