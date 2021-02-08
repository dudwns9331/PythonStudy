# UCPC는 무엇의 약자일까?

"""
2021-02-08 오전 9:05
안영준

문제 링크 : https://www.acmicpc.net/problem/15904

블로그 참조
"""

s = input()
alp = ['U', 'C', 'P', 'C']
i = 0
for a in alp:
    if a in s:
        i += 1
        s = s[s.index(a) + 1:]
    else:
        print('I hate UCPC')
        break
if i == 4:
    print('I love UCPC')
