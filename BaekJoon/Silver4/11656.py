# 접미사 배열

"""
2021-03-02 오후 8:27
안영준

문제 : https://www.acmicpc.net/problem/11656

"""

string = list(input())

length = len(string)

result = list()

for i in range(length):
    result.append(''.join(map(str, string)))
    string.pop(0)

result.sort()

print('\n'.join(map(str, result)))
