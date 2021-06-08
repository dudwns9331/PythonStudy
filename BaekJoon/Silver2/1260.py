# DFS와 BFS

"""
2021-06-08 오전 9:08
안영준

문제 : https://www.acmicpc.net/problem/1260
"""

import sys


def depth_first_search(v: int):
    # 시작 정점 출력
    print(v, end=' ')
    # 방문 행렬에 표시
    visit[v] = 1
    # 만약 방문하지 않았고 그래프에 있는 정점이면 깊이우선 탐색 재귀
    for i in range(1, N + 1):
        if visit[i] == 0 and graph[v][i] == 1:
            depth_first_search(i)


def breadth_first_search(v: int):
    # 순서대로 출력할 queue
    queue = [v]
    visit[v] = 0
    # queue가 비지 않았으면
    while (queue):
        v = queue[0]
        # 출력 후 queue에서 제거
        print(v, end=' ')
        del queue[0]
        # 방문했고 그래프에 표시된 정점
        for i in range(1, N + 1):
            if visit[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 0


input = lambda: sys.stdin.readline().rstrip()

# N = 정점의 개수, M = 간선의 개수, V = 시작정점
N, M, V = map(int, input().split())

# 그래프 초기화 시켜주기
graph = [[0] * (N + 1) for i in range(N + 1)]
visit = [0 for _ in range(N + 1)]

for i in range(M):
    # 입력 받은 정점 그래프에 표시하기
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

depth_first_search(V)
print()
breadth_first_search(V)
