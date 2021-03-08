# 스택

"""
2021-03-08 오전 9:01
안영준

문제 : https://www.acmicpc.net/problem/10828

"""

import sys

input = lambda: sys.stdin.readline()

stack = list()

for i in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) != 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)
