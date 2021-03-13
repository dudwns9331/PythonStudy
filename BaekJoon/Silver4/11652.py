# 카드

"""
2021-03-13 오후 1:27
안영준

문제 : https://www.acmicpc.net/problem/11652

"""

import sys
from collections import Counter

input = lambda: sys.stdin.readline()

N = int(input())
result = [int(input()) for _ in range(N)]
count = Counter(sorted(result))
print(count.most_common(1)[0][0])
