# 좋은 단어

"""
2021-03-20 오후 3:55
안영준

문제 : https://www.acmicpc.net/problem/3986
"""

import sys

input = lambda: sys.stdin.readline()

count = 0
for _ in range(int(input())):
    string = input()
    stack = list()
    for c in string:
        if c == 'A':
            if len(stack) == 0 or (stack != [] and stack[-1] != 'A'):
                stack.append(c)
            else:
                stack.pop()
        if c == 'B':
            if len(stack) == 0 or (stack != [] and stack[-1] != 'B'):
                stack.append(c)
            else:
                stack.pop()
    if not stack:
        count += 1
print(count)
