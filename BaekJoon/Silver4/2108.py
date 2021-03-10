# 통계학

"""
2021-03-10 오후 4:00
안영준

문제 : https://www.acmicpc.net/problem/2108

"""

import sys
from collections import Counter

number = list()

for i in range(int(sys.stdin.readline())):
    number.append(int(sys.stdin.readline()))

number = sorted(number)

number_count = Counter(number).most_common()

print(round(sum(number) / len(number)))
print(number[len(number) // 2])

if len(number_count) > 1:
    if number_count[0][1] == number_count[1][1]:
        print(number_count[1][0])
    else:
        print(number_count[0][0])
else:
    print(number_count[0][0])
print(number[-1] - number[0])
