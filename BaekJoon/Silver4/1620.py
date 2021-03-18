# 나는야 포켓몬 마스터

"""
2021-03-18 오전 9:46
안영준

문제 : https://www.acmicpc.net/problem/1620
"""

import sys

input = lambda: sys.stdin.readline()

N, M = map(int, input().split())

number_pokemon = 1

pokemon_dict1 = {}
pokemon_dict2 = {}

for _ in range(N):
    name = str(sys.stdin.readline()).strip()
    pokemon_dict1[number_pokemon] = name
    pokemon_dict2[name] = number_pokemon
    number_pokemon += 1

answer = []
for _ in range(M):
    pokemon = str(sys.stdin.readline()).strip()
    try:
        print(pokemon_dict1[int(pokemon)])
    except:
        print(pokemon_dict2[pokemon])
