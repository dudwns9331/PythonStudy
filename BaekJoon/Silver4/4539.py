# 반올림

"""
2021-03-30 오후 8:09
안영준

문제 : https://www.acmicpc.net/problem/4539
"""
for i in range(int(input())):
    number = list(input())
    for j in range(len(number) - 1, 0, -1):
        if int(number[j]) >= 5:
            number[j - 1] = str(int(number[j - 1]) + 1)
        number[j] = '0'

    for k in range(len(number)):
        print(number[k], end='')
    print()
