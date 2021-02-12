# 수 정렬하기 4

"""
2021-02-12 오후 12:12
안영준

문제 : https://www.acmicpc.net/problem/11931

"""

import sys

N = int(sys.stdin.readline())

array = list()

for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
print('\n'.join(map(str, array[::-1])))
