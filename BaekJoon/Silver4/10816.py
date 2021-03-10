# 숫자 카드 2

"""
2021-03-10 오후 4:31
안영준

문제 : https://www.acmicpc.net/problem/10816

"""

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
search_card = list(map(int, input().split()))

card = Counter(card)

for i in search_card:
    print(card[i], end=" ")
