# 아시아 정보올림피아드

"""
2021-02-17 오후 11:21
안영준

문제 : https://www.acmicpc.net/problem/2535

이게 왜 맞음?

"""

N = int(input())
students = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: -x[2])

print(*students[0][:2])
print(*students[1][:2])

if students[0][0] == students[1][0]:
    print(*students[3][:2])
else:
    print(*students[2][:2])
