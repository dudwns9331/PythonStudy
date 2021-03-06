# 카드

"""
2021-03-05 오후 5:22
안영준

문제 : https://www.acmicpc.net/problem/2164

덱 이용
"""

import collections

N = int(input())

card = collections.deque([i for i in range(1, N + 1)])

while True:
    if len(card) == 1:
        break
    else:
        card.popleft()
        card.rotate(-1)

print(card[0])
