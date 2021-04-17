# 팩토리얼 0의 개수

"""
2021-04-17 오후 4:52
안영준

문제 : https://www.acmicpc.net/problem/1676
"""

import math
import sys

input = lambda: sys.stdin.readline().rstrip()

result = str(math.factorial(int(input())))

count = 0

for i in range(1, len(result)):
    if result[-i] == '0':
        count += 1
    else:
        break

print(count)
