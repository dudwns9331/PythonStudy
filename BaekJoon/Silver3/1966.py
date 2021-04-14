# 프린터 큐

"""
2021-04-13 오전 9:05
안영준

문제 : https://www.acmicpc.net/problem/1966
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

for i in range(eval(input())):

    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    s_ = [0 for _ in range(N)]
    s_[M] = 1
    count = 0

    while True:
        if number[0] == max(number):
            count += 1
            if s_[0] == 1:
                print(count)
                break
            else:
                number.pop(0)
                s_.pop(0)
        else:
            number.append(number[0])
            number.pop(0)
            s_.append(s_[0])
            s_.pop(0)
