# 피자

"""
2021-03-28 오후 4:59
안영준

문제 : https://www.acmicpc.net/problem/14606
"""


def cal_happy(n: int):
    half = round(n / 2)
    r = n - half
    result = half * r

    if n == 1:
        return 0

    if half != 1:
        result += cal_happy(half)
    if r != 1:
        result += cal_happy(r)

    return result


N = int(input())

print(cal_happy(N))
