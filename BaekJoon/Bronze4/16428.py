# A/B - 3

"""
2021-02-10 오전 1:24
안영준

문제 : https://www.acmicpc.net/problem/16428
"""

a, b = map(int, input().split())
if a > 0 and b < 0:
    print(-(a // abs(b)))
    print(a % abs(b))
elif a < 0 and b > 0:
    print(-(abs(a) // b + 1))
    print(b - (abs(a) % b))
elif a < 0 and b < 0:
    print(abs(a) // abs(b) + 1)
    print(abs(b) - (abs(a) % abs(b)))
else:
    print(a // b)
    print(a % b)
