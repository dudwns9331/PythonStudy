# 세 개의 소수 문제

"""
2021-05-27 오전 9:51
안영준

문제 : https://www.acmicpc.net/problem/11502
"""

import itertools
import math
import sys


def isPrime(number: int):
    if number == 1:
        return False
    else:
        for j in range(2, int(math.sqrt(number)) + 1):
            if number % j == 0:
                return False
        return True


def findPrime(number_list: list):
    prime = list()
    for k in number_list:
        if isPrime(k):
            prime.append(k)
    return prime


input = lambda: sys.stdin.readline().rstrip()

T = int(input())

count = 0

for i in range(T):
    N = int(input())
    numbers = [int(x) + 1 for x in range(N - 1)]
    result = findPrime(numbers)
    perm = list(itertools.combinations_with_replacement(result, 3))
    for prime_set in perm:
        if sum(prime_set) == N:
            count += 1
            print(*prime_set)
            break
        if count < 1:
            print(0)
            count = 0
