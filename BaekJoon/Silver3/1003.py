# 피보나치 함수

"""
2021-04-05 오전 9:20
안영준

문제 : https://www.acmicpc.net/problem/1003
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

Test = eval(input())

for i in range(Test):
    n = eval(input())
    zero_count = 1
    one_count = 0
    temp = 0
    for _ in range(n):
        temp = one_count
        one_count = one_count + zero_count
        zero_count = temp
    print(zero_count, one_count)
