# 연결 요소의 개수

"""
2021-06-14 오후 3:05
안영준

문제 : https://www.acmicpc.net/problem/11724
"""

import sys

# 재귀 제한걸어주기 안해주면 런타임 오류
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# 그래프 초기화 시켜주기
graph = [[0] * (N + 1) for i in range(N + 1)]
visit = [0 for _ in range(N + 1)]
count = 0


# 깊이 우선 탐색
def depth_first_search(index):
    visit[index] = 1
    for k in range(1, N + 1):
        if graph[index][k] == 1 and visit[k] == 0:
            depth_first_search(k)


# 그래프 입력 받기
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, N + 1):
    # 깊이 우선 탐색이 완료된 것은 연결된 그래프임.
    if visit[i] == 0:
        depth_first_search(i)
        count += 1

print(count)
