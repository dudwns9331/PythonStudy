# 쇠막대기

"""
2021-04-15 오후 4:26
안영준

문제 : https://www.acmicpc.net/problem/10799
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

string = list(input())
stack = list()

result = 0

for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:
        if string[i - 1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
