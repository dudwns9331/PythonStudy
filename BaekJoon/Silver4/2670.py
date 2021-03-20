# 연속부분최대곱

"""
2021-03-20 오후 3:35
안영준

문제 : https://www.acmicpc.net/problem/2670
"""

import sys

input = lambda: sys.stdin.readline()

number = list()
for i in range(int(input())):
    number.append(float(input()))

for j in range(1, len(number)):
    number[j] = max(number[j], number[j] * number[j - 1])

print("%.3f" % (max(number)))
