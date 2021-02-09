# 암호

"""
2021-02-10 오전 12:33
안영준

문제 : https://www.acmicpc.net/problem/1855

"""

K = int(input())
string = input()
result = list()

answer = list()

count = 0
is_even = 1
for i in range(count, len(string) + count, K):
    if is_even % 2 == 0:
        result.append(list(string[count:count + K][::-1]))
    else:
        result.append(list(string[count:count + K]))
    count += K
    is_even += 1

for i in range(K):
    for j in range(len(result)):
        answer.append(result[j][i])

print(''.join(map(str, answer)))
