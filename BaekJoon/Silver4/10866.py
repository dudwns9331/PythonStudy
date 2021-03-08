# 덱

"""
2021-03-08 오전 9:24
안영준

https://www.acmicpc.net/problem/10866

"""
import sys

input = lambda: sys.stdin.readline()

dequeue = list()

for i in range(int(input())):
    command = input().split()
    if command[0] == 'push_back':
        dequeue.append(command[1])
    elif command[0] == 'push_front':
        dequeue.insert(0, command[1])
    elif command[0] == 'pop_back':
        if len(dequeue) != 0:
            print(dequeue.pop())
        else:
            print(-1)
    elif command[0] == 'pop_front':
        if len(dequeue) != 0:
            print(dequeue.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dequeue))
    elif command[0] == 'empty':
        if len(dequeue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dequeue) != 0:
            print(dequeue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(dequeue) != 0:
            print(dequeue[len(dequeue) - 1])
        else:
            print(-1)
