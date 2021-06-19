# 로또

"""
2021-06-19 오후 2:52
안영준

문제 : https://www.acmicpc.net/problem/6603
"""

import itertools
import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    Test = list(map(int, input().split()))

    if len(Test) == 1:
        break
        
    number_set = Test[1:]
    result = list(itertools.combinations(number_set, 6))

    for i in result:
        for j in i:
            print(j, end=' ')
        print()
    print()
