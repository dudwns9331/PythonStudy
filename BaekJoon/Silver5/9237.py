# 이장님 초대

"""
2021-02-19 오전 1:51
안영준

문제 : https://www.acmicpc.net/problem/9237

"""

N = int(input())
tree = list(map(int, input().split(" ")))
day = N
tree = sorted(tree)
for i in range(N):
    tree[i] -= i
day += max(tree) + 1
print(day)
