# 베르트랑 공준

"""
2021-06-18 오전 9:13
안영준

문제 : https://www.acmicpc.net/problem/4948
"""

import math
import sys


def isPrime(number: int):
    if number == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True


input = lambda: sys.stdin.readline().rstrip()

count = 0

while True:
    N = int(input())
    if N == 0:
        break
    for i in range(N + 1, N * 2 + 1):
        if isPrime(i):
            count += 1
    print(count)
    count = 0
