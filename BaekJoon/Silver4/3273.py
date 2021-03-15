# 두 수의 합

"""
2021-03-15 오전 11:59
안영준

문제 :

"""

n = int(input())
number = sorted(map(int, input().split()))
x = int(input())

count = 0

i = 0
j = n - 1

while i != j:
    s = number[i] + number[j]
    if s == x:
        count += 1
        i += 1
    elif s > x:
        j -= 1
    else:
        i += 1

print(count)
