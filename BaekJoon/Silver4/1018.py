# 체스판 다시 칠하기

"""
2021-04-02 오후 11:14
안영준

문제 : https://www.acmicpc.net/problem/10181
"""
n, m = map(int, input().split())
l = []
min_value = []

for _ in range(n):
    l.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        index1 = 0
        index2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):
                if (j + b) % 2 == 0:
                    if l[b][j] != 'W':
                        index1 += 1
                    if l[b][j] != 'B':
                        index2 += 1
                else:
                    if l[b][j] != 'B':
                        index1 += 1
                    if l[b][j] != 'W':
                        index2 += 1
        min_value.append(index1)
        min_value.append(index2)

print(min(min_value))
