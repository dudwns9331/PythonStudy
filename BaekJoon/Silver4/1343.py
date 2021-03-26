# 폴리오미노

"""
2021-03-26 오전 12:33
안영준

문제 : https://www.acmicpc.net/problem/1343
"""

import sys

input = lambda: sys.stdin.readline()

string = input()

A = "AAAA"
B = "BB"

string = string.replace("XXXX", A)
string = string.replace("XX", B)

if "X" in string:
    print(-1)
else:
    print(string)
