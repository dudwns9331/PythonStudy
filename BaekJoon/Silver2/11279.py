# 최대 힙

"""
2021-06-26 오후 3:01
안영준

문제 : https://www.acmicpc.net/problem/11279
"""
import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

numbers = int(input())

max_heap = list()

for i in range(numbers):
    number = int(input())
    if number != 0:
        heapq.heappush(max_heap, -number)
    else:
        try:
            print(-1 * heapq.heappop(max_heap))
        except:
            print(0)
