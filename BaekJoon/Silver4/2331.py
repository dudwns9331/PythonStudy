# 반복수열

"""
2021-03-21 오후 4:29
안영준

문제 : https://www.acmicpc.net/problem/2331
"""


def pow_cal(number: str):
    pow_result = 0
    for j in range(len(number)):
        pow_result = pow_result + pow(int(number[j]), P)

    return str(pow_result)


A, P = map(int, input().split())

A = str(A)

result = list()

result.append(A)

index = 0

while True:
    if pow_cal(result[-1]) in result:
        index = result.index(pow_cal(result[-1]))
        break
    else:
        result.append(pow_cal(result[-1]))

print(index)
