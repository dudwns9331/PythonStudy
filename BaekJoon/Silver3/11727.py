# 2 x n 타일링 2

"""
2021-04-11 오후 7:03
안영준

문제 : https://www.acmicpc.net/problem/11727
"""
# 2xn 타일링

"""
2021-04-07 오후 3:34
안영준

문제 : https://www.acmicpc.net/problem/11726
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

fibonacci = [0, 1, 3]

for i in range(3, 1001):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2] * 2)

print(fibonacci[eval(input())] % 10007)
