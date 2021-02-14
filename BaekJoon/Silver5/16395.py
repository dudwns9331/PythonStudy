# 파스칼의 삼각형

"""
2021-02-14 오후 3:35
안영준

문제 : https://www.acmicpc.net/problem/16395

"""

import math

n, k = map(int, input().split())

print(math.comb(n - 1, k - 1))
