# 인기 투표

"""
2021-02-16 오전 12:46
안영준

문제 : https://www.acmicpc.net/problem/11637

"""

import sys

Test = int(sys.stdin.readline())

for i in range(Test):
    result = list()
    for j in range(int(sys.stdin.readline())):
        result.append(int(sys.stdin.readline()))
    if result.count(max(result)) > 1:
        print('no winner')
    else:
        if sum(result) // 2 < max(result):
            print(f'majority winner {result.index(max(result)) + 1}')
        else:
            print(f'minority winner {result.index(max(result)) + 1}')
