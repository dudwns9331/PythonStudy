# 캠핑

"""
2021-02-22 오후 8:43
안영준

문제 : https://www.acmicpc.net/problem/4796

"""

count = 0
while 1:
    count += 1
    l, p, v = map(int, input().split()
                  )
    if l == 0 and p == 0 and v == 0:
        break
    if v % p >= l:
        result = v // p * l + l
    else:
        result = v // p * l + v % p

    print("Case " + str(count) + ": " + str(result))
