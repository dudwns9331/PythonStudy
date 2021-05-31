# 단어 뒤집기2

"""
2021-05-30 오후 1:13
안영준

문제 : https://www.acmicpc.net/problem/17413
"""

import sys

Strings = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(Strings):
    if Strings[i] == "<":
        i += 1
        while Strings[i] != ">":
            i += 1
        i += 1
    elif Strings[i].isalnum():
        start = i
        while i < len(Strings) and Strings[i].isalnum():
            i += 1
        tmp = Strings[start:i]
        tmp.reverse()
        Strings[start:i] = tmp
    else:
        i += 1

print("".join(Strings))
