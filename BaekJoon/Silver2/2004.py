# 조합 0의 개수

"""
2021-07-03 오후 8:26
안영준

문제 : https://www.acmicpc.net/problem/2004
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())


def count(n: int, k: int):
    count = 0
    while n:
        n //= k
        count += n
    return count


f_count = count(N, 5) - count(M, 5) - count(N - M, 5)
t_count = count(N, 2) - count(M, 2) - count(N - M, 2)

result = min(f_count, t_count)

print(result)
