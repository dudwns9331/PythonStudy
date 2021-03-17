# 베스트셀러

"""
2021-03-16 오후 5:44
안영준

문제 : https://www.acmicpc.net/problem/1302
"""
import collections
import sys

input = lambda: sys.stdin.readline()

result = list()
count_list = list()

for i in range(int(input())):
    result.append(input().rstrip())

result.sort()

count_list = collections.Counter(result).most_common()

print(count_list[0][0])
