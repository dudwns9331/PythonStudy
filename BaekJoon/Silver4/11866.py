# 요세푸스 문제 0

"""
2021-03-01 오전 11:11
안영준

문제 : https://www.acmicpc.net/problem/11866

"""
N, K = map(int, input().split())

list1 = [i for i in range(1, N + 1)]
result = []
temp = K - 1

for i in range(N):
    if len(list1) > temp:
        result.append(list1.pop(temp))
        temp += K - 1

    elif len(list1) <= temp:
        temp = temp % len(list1)
        result.append(list1.pop(temp))
        temp += K - 1

print("<", end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print("%s, " % i, end='')
print(">")
