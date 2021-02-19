# 줄 세우기

"""
2021-02-20 오전 12:47
안영준

문제 : https://www.acmicpc.net/problem/11536

"""

N = int(input())

result = list()

for i in range(N):
    result.append(list(input()))

if sorted(result) == result:
    print('INCREASING')
elif sorted(result, reverse=True) == result:
    print('DECREASING')
else:
    print("NEITHER")
