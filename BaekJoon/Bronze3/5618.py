# 공약수

"""
2021-01-11 오후 11:18
안영준

문제
자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 2 또는 3이다. 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다. 모든 자연수는 108 이하이다.

출력
입력으로 주어진 n개 수의 공약수를 한 줄에 하나씩 증가하는 순서대로 출력한다.

답안 참고함. 런타임 에러, 시간초과 오지게 나옴

"""

import sys


def cal(a, b):
    if a == 0:
        return b
    return cal(b % a, a)


N = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))
g = cal(result[0], cal[result[1], result[-1]])

for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
print(g)
