# 다음 순열

"""
2021-04-29 오전 10:27
안영준

문제 : https://www.acmicpc.net/problem/10972
"""

# import sys
#
# from itertools import permutations
#
# input = lambda: sys.stdin.readline().rstrip()
#
# N = int(input())
#
# number = list(map(int, input().split()))
#
# perm = permutations(number, N)
#
# result = list(perm)
#
# result.sort()
#
# if result.index(tuple(number)) == len(result) - 1:
#     print(-1)
# else:
#     print(' '.join(map(str, result[result.index(tuple(number)) + 1])))


# next Permutation ?
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s = list(map(int, input().split()))
x = 0
for i in range(n - 1, 0, -1):
    if s[i - 1] < s[i]:
        x = i - 1
        break
for i in range(n - 1, 0, -1):
    if s[x] < s[i]:
        s[x], s[i] = s[i], s[x]
        s = s[:x + 1] + sorted(s[x + 1:])
        print(*s)
        exit()
print(-1)
