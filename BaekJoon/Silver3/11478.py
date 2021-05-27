# 서로 다른 부분 문자열의 개수

"""
2021-05-27 오전 11:02
안영준

문제 : https://www.acmicpc.net/problem/11478
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

string = input()
result = list()

for i in range(len(string)):
    for j in range(len(string) - i):
        result.append(string[j:j + i + 1])

print(len(set(result)))
