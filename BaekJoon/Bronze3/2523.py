# 별 찍기 - 13

"""
2021-01-06 오후 10:10
안영준

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

"""

N = int(input())

j = 1
k = 0

for i in range(2 * N - 1):
    if j >= N:
        print('*' * k)
        k += -1

    else:
        print('*' * j)
        j += 1
        k = j
