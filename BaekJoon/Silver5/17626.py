# Four Squares

"""
2021-02-19 오전 1:04
안영준

문제 : https://www.acmicpc.net/problem/17626

미해결

"""

import math

N = int(input())

count = 0

while True:
    if N == 0:
        break
    else:
        N = N - int(math.sqrt(N)) ** 2
        print(N)
        count += 1

print(count)
