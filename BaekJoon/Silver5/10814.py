# 나이순 정렬

"""
2021-02-13 오후 11:12
안영준

문제 : https://www.acmicpc.net/problem/10814

"""

user = list()

for i in range(int(input())):
    age, name = map(str, input().split())
    user.append((age, name))

user = sorted(user, key=lambda x: int(x[0]))

count = 0
for k in user:
    print(user[count][0], user[count][1])
    count += 1
