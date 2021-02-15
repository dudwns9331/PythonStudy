# 성적 통계

"""
2021-02-15 오전 10:48
안영준

문제 : https://www.acmicpc.net/problem/5800

"""


def gap(array: list):
    array.sort()
    gap_value = 0
    for j in range(len(array) - 1):
        if gap_value < array[j + 1] - array[j]:
            gap_value = array[j + 1] - array[j]

    return gap_value


K = int(input())

for i in range(1, K + 1):
    array = list(map(int, input().split()))
    array = array[1:]
    max_value = max(array)
    min_value = min(array)
    gap_value = gap(array)

    print(f'Class {i}')
    print(f'Max {max_value}, Min {min_value}, Largest gap {gap_value}')
