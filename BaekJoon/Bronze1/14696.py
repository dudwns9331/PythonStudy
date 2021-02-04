# 딱지놀이

"""
2021-02-03 오후 10:57
안영준

https://www.acmicpc.net/problem/14696 설명

만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.

별 > 동그라미 > 네모 > 세모
4   >   3   >   2   >   1

"""

N = int(input())

a_count = list()
b_count = list()

for i in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = a[1:]
    b = b[1:]

    for j in range(4, 0, -1):
        a_count.append(a.count(j))

    for j in range(4, 0, -1):
        b_count.append(b.count(j))

    for j in range(4):
        if a_count[j] > b_count[j]:
            print('A')
            a_count = []
            b_count = []
            break
        elif a_count[j] < b_count[j]:
            print('B')
            a_count = []
            b_count = []
            break
        else:
            if j == 3:
                print("D")
                a_count = []
                b_count = []
            else:
                continue
