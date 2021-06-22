# 잃어버린 괄호

"""
2021-06-21 오후 7:18
안영준

문제 : https://www.acmicpc.net/problem/1541
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

# - 를 기준으로 나눈다.
minus = input().split('-')
number = list()

for i in minus:
    count = 0
    plus = i.split('+')
    for j in plus:
        count += int(j)
    number.append(count)

n = number[0]

for i in range(1, len(number)):
    n -= number[i]
    
print(n)
