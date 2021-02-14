# 수 정렬하기 5

"""
2021-02-14 오후 3:38
안영준

문제 : https://www.acmicpc.net/problem/15688

"""

import sys

result = list()

for i in range(int(sys.stdin.readline())):
    result.append(int(sys.stdin.readline()))

print('\n'.join(map(str, sorted(result))))
