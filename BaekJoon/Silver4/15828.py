# Router

"""
2021-04-02 오후 1:41
안영준

문제 : https://www.acmicpc.net/problem/15828
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

result = list()

N = int(input())

while True:

    number = int(input())

    if number == -1:
        break
    else:
        if number == 0:
            result.pop(0)
        elif len(result) >= N:
            continue
        else:
            result.append(number)

if len(result) == 0:
    print("empty")
else:
    print(' '.join(map(str, result)))
