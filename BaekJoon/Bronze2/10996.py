# 별찍기 - 21

"""
2021-01-17 오후 6:53
안영준

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 차례대로 별을 출력한다.

"""

N = int(input())

for i in range(N):
    for j in range(N):
        if j % 2 == 0:
            print("* ", end='')
    print()
    for k in range(N):
        if k % 2 != 0:
            print(" *", end='')
    print()
