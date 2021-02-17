# 방 번호

"""
2021-02-18 오전 12:01
안영준

문제 : https://www.acmicpc.net/problem/1475

"""

import math

n = input()

number = [0] * 10

for i in range(10):
    number[i] = n.count(str(i))

if number.index(max(number)) == 6 or number.index(max(number)) == 9:
    print(math.ceil((number[6] + number[9]) / 2))
else:
    print(max(number))
