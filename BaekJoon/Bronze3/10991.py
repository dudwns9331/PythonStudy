# 별찍기 - 16

"""
2021-01-08 오후 2:32
안영준

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

"""

N = int(input())

j = N - 1

for i in range(1, N + 1):
    print(' ' * j, end='')
    print('* ' * i)
    j -= 1