# 시리얼 번호

"""
2021-05-14 오후 8:16
안영준

문제 : https://www.acmicpc.net/problem/1431
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

result = list()

for i in range(int(input())):
    count = 0
    serial = input()
    for j in serial:
        if j.isdigit():
            count += int(j)
    result.append((serial, count))

result = sorted(result, key=lambda x: (len(x), x[1], x[0]))

for k in result:
    print(k[0])
