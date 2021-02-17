# 거스름돈

"""
2021-02-17 오후 11:38
안영준

문제 : https://www.acmicpc.net/problem/14916

"""

n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    count = -1
    for i in range(n // 5, -1, -1):
        temp = n - 5 * i
        if temp % 2 == 0:
            count += 1 + i + temp // 2
            break
    print(count)
