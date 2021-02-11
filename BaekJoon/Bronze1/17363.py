# 우유가 넘어지면?

"""
2021-02-11 오전 10:10
안영준

문제 : https://www.acmicpc.net/problem/17363

"""

N, M = map(int, input().split())
b = [[0] * N for _ in range(M)]
f = {
    '.': '.',
    'O': 'O',
    '-': '|',
    '|': '-',
    '/': '\\',
    '\\': '/',
    '^': '<',
    '<': 'v',
    'v': '>',
    '>': '^'
}
for i in range(N):
    data = input()
    for j in range(M):
        b[M - j - 1][i] = f[data[j]]
for e in b:
    print(*e, sep='')
