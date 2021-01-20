# 별찍기 - 20

"""
2021-01-20 오후 3:56
안영준

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 차례대로 별을 출력한다.

"""

N = int(input())

for i in range(1, N + 1):
    if i % 2 == 1:
        for j in range(1, N + 1):
            print("* ", end='')
    else:
        for k in range(1, N + 1):
            print(" *", end='')
    print()
