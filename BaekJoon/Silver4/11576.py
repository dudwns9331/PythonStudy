# Base Conversion

"""
2021-03-22 오후 3:22
안영준

문제 : https://www.acmicpc.net/problem/11576
"""

A, B = map(int, input().split())
m = input()
before = list(map(int, input().split()))

total = 0
power = 0

for b in before[::-1]:
    total += (b * (A ** power))
    power += 1

result = list()

while total:
    result.append(str(total % B))
    total //= B

print(' '.join(result[::-1]))
