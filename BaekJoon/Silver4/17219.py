# 비밀번호 찾기

"""
2021-03-05 오전 12:10
안영준

문제 : https://www.acmicpc.net/problem/17219

"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
result = dict(sys.stdin.readline().rstrip().split() for _ in range(n))

for _ in range(m):
    site = input()
    print(result.get(site))
