# 점화석

"""
2021-03-15 오후 9:11
안영준

문제 : https://www.acmicpc.net/problem/13699
"""

result = list()

result.append(1)

n = int(input())

tmp = 0
for i in range(1, 36):
    for j in range(0, i):
        tmp += (result[i - 1 - j] * result[j])
    result.append(tmp)
    tmp = 0

print(result[n])
