# 나이트의 이동

"""
2021-06-25 오후 10:24
안영준

문제 : https://www.acmicpc.net/problem/7562
"""

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# 시계 방향으로 나이트가 이동할 수 있는 경우의 수
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


# 너비우선 탐색
def bfs(positionX, positionY, destinationX, destinationY):
    # 덱 선언
    queue = deque()
    # 덱에 현재 위치 넣음
    queue.append([positionX, positionY])
    # 시퀀스에 큐에 있었던 좌표 표시
    sequence[positionX][positionY] = 1
    while queue:
        a, b = queue.popleft()
        if a == destinationX and b == destinationY:
            print(sequence[destinationX][destinationY] - 1)
            return
        for j in range(8):
            x = a + dx[j]
            y = b + dy[j]
            if 0 <= x < l and 0 <= y < l and sequence[x][y] == 0:
                queue.append([x, y])
                sequence[x][y] = sequence[a][b] + 1


# 태스트 케이스의 개수
T = int(input())

for i in range(T):
    # 체스판 한 변의 길이 l * l의 체스판의 크기를 갖는다.
    l = int(input())
    # 나이트가 현재 있는 칸
    positionX, positionY = map(int, input().split())
    # 나이트가 가야하는 목적지 칸
    destinationX, destinationY = map(int, input().split())

    sequence = [[0] * l for _ in range(l)]
    bfs(positionX, positionY, destinationX, destinationY)
