# 행렬 덧셈

"""
2021-02-01 오후 11:05
안영준

문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의
원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

"""

N, M = map(int, input().split())

a_result = list()
b_result = list()
for i in range(N):
    a_result.append(list(map(int, input().split())))

for j in range(N):
    b_result.append(list(map(int, input().split())))

c_result = []

for k in range(N):
    result = []
    for x in range(M):
        result.append(a_result[k][x] + b_result[k][x])
    c_result.append(result)

for i in c_result:
    print(' '.join(map(str, i)))
