# 주유소

"""
2021-03-21 오후 5:02
안영준

문제 : https://www.acmicpc.net/problem/13305
"""

N = int(input())

distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

cost = cost[:-1]

result = 0

min_cost = min(cost)

if cost.index(min_cost) == 0:
    print(sum(distance))
else:
    for i in range(cost.index(min_cost)):
        result = result + cost[i] * distance[i]
    result += min_cost * sum(distance[cost.index(min_cost):])
    print(result)
