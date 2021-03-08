# 숫자 카드

"""
2021-03-08 오전 9:31
안영준

문제 : https://www.acmicpc.net/problem/10815

"""

import sys

input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
m = int(input())
s_ = list(map(int, input().split()))
s.sort()
for i in s_:
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if 0 <= mid < n:
            if s[mid] < i:
                low = mid + 1
            else:
                high = mid - 1
        else:
            break
    if 0 <= high + 1 < n:
        if s[high + 1] == i:
            print(1, end=" ")
        else:
            print(0, end=" ")
    else:
        print(0, end=" ")
