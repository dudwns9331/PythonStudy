# 생일

"""
2021-02-14 오후 3:42
안영준

문제 : https://www.acmicpc.net/problem/5635

"""

import sys

result = list()

for i in range(int(sys.stdin.readline())):
    result.append(list(map(str, input().split())))

result = sorted(result, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(result[len(result) - 1][0])
print(result[0][0])
