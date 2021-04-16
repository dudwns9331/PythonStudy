# 나무 자르기

"""
2021-04-16 오후 9:39
안영준

문제 : https://www.acmicpc.net/problem/2805
"""

# 이분탐색 이용

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

trees = list(map(int, input().split()))

left, right, result = 0, max(trees), 0

while left <= right:
    # 가장 큰 수의 절반이 들어간다?
    mid = (left + right) // 2
    tree = 0

    # 중간값을 tree 값에 넣는다.
    for i in range(N):
        if mid < trees[i]:
            # 원래 나무의 길이에 중간값을 뺀 값을 넣는다.
            tree += trees[i] - mid

    # 만약에 나무의 길이가 M(원하는 길이)보다 길면
    if tree >= M:
        # 그 결과는 mid(중간값이 되고)
        result = mid
        # 오른쪽 절반의 이분 탐색을 통해 다시 수행한다.
        left = mid + 1
    # 아닐경우 왼쪽 절반을 이분 탐색한다.
    elif tree < M:
        right = mid - 1

print(result)
