# 큐

"""
2021-03-08 오전 9:13
안영준

문제 : https://www.acmicpc.net/problem/10845

"""

import sys

input = lambda: sys.stdin.readline()

queue = list()

for i in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(queue) != 0:
            print(queue[len(queue) - 1])
        else:
            print(-1)
