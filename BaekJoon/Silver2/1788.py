# 피보나치 수의 확장

"""
2021-07-15 오후 5:44
안영준

문제 : https://www.acmicpc.net/problem/1788
"""

N = int(input())
sequence = [0, 1]
for i in range(2, abs(N) + 1):
    sequence.append((sequence[i - 1] + sequence[i - 2]) % 1000000000)
if N % 2 == 0 and N < 0:
    print(-1)
elif N == 0:
    print(0)
else:
    print(1)
print(sequence[abs(N)])
