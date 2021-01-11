# 2의 제곱인가?

"""
2021-01-11 오전 12:14
안영준

문제
자연수 N이 주어졌을 때, 2의 제곱수면 1을 아니면 0을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 2^30)이 주어진다.

출력
N이 2의 제곱수면 1을 아니면 0을 출력하는 프로그램을 작성하시오.

"""

N = int(input())

result = list()

for i in range(31):
    result.append(2 ** i)

if N in result:
    print(1)
else:
    print(0)
