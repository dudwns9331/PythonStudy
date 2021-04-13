# 스택 수열

"""
2021-04-12 오후 4:11
안영준

문제 : https://www.acmicpc.net/problem/1874
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

stack = []
operation = []
count = 1
temp = True

for i in range(eval(input())):
    number = eval(input())
    while count <= number:
        stack.append(count)
        operation.append('+')
        count += 1
    if stack[-1] == number:
        stack.pop()
        operation.append('-')
    else:
        temp = False

if temp:
    for i in operation:
        print(i)
else:
    print('NO')
