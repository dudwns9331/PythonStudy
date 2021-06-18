# K번째 소수

"""
2021-06-12 오후 10:52
안영준

문제 : https://www.acmicpc.net/problem/15965
"""

import math
import sys

input = lambda: sys.stdin.readline().rstrip()


def isPrime(number: int):
    if number == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True


N = int(input())

result = list()
count = 1

while len(result) != N:
    if isPrime(count):
        result.append(count)
    count += 1

print(result[-1])
