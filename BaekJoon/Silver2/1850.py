# 최대공약수

"""
2021-07-08 오전 11:05
안영준

문제 : https://www.acmicpc.net/problem/1850
"""
import math
import sys

input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())

print('1' * math.gcd(a, b))
