# 공약수

"""
2021-05-02 오후 2:50
안영준

문제 : https://www.acmicpc.net/problem/2436
"""
import math
import sys

input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())

result_a = 0
result_b = 0

b /= a

i = 1
while i ** 2 <= b:
    if b % i == 0:
        if math.gcd(i, int(b / i)) == 1:
            result_a = i
            result_b = int(b / i)
    i += 1

print(result_a * a, result_b * a)
