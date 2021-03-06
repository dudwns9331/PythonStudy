# Darius님 한타 안 함?

"""
2021-02-10 오전 1:30
안영준

문제 : https://www.acmicpc.net/problem/20499

"""

K, D, A = map(str, input().split('/'))

if int(K) + int(A) < int(D) or int(D) == 0:
    print('hasu')
else:
    print('gosu')
