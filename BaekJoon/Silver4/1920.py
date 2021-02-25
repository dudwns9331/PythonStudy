# 수 찾기

"""
2021-02-25 오후 12:36
안영준

문제 : https://www.acmicpc.net/problem/1920

"""

import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    if i in a:
        print('1')
    else:
        print('0')
