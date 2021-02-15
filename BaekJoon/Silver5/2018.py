# 수들의 합

"""
2021-02-16 오전 12:36
안영준

문제 : https://www.acmicpc.net/problem/2018

블로그 참조.
등차수열의 합 공식 적용
이걸 어떻게 알아?

"""

N = int(input())
count = 0
for i in range(1, N + 1):
    if i * 2 <= N * 2 - i ** 2 + i and (N * 2 - i ** 2 + i) % (i * 2) == 0:
        count += 1
print(count)
