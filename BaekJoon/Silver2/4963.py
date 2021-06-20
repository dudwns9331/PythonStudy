# 섬의 개수

"""
2021-06-20 오후 11:01
안영준

문제 : https://www.acmicpc.net/problem/4963
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

# 8 방향 탐색을 위해서 상하좌우 각 대각선을 지정한다.
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(i: int, j: int):
    map_list[i][j] = 0
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and map_list[x][y] == 1:
                map_list[x][y] = 0
                queue.append([x, y])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    map_list = list()
    count = 0
    for i in range(h):
        map_list.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if map_list[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
