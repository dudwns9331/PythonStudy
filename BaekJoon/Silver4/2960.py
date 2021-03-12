# 에라토스테네스의 체

"""
2021-03-11 오후 4:31
안영준

문제 : https://www.acmicpc.net/problem/2960

"""


def getPrime(array: list):
    count = 0
    for i in array:
        for j in range(1, array[-1] + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            return i


import sys

input = lambda: sys.stdin.readline()
N, K = map(int, input().split())

number = [i for i in range(2, N + 1)]

result_count = 0
result = 0
while True:
    prime = getPrime(number)
    for i in range(prime, number[-1] + 1, prime):
        if i in number:
            number.remove(i)
            result = i
            result_count += 1
            if result_count == K:
                break
        else:
            continue
    if result_count == K:
        print(result)
        break
