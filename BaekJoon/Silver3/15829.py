# Hashing

"""
2021-04-12 오후 4:07
안영준

문제 : https://www.acmicpc.net/problem/15829
"""
N = int(input())
string = input()
result = 0

for i in range(N):
    result += (ord(string[i]) - 96) * (31 ** i)
print(result % 1234567891)
