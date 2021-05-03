# 소수 구하기

"""
2021-05-01 오후 2:40
안영준

문제 : https://www.acmicpc.net/problem/1929
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


M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
