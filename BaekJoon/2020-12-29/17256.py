# 달달함이 넘쳐흘러

"""
2020-12-29-19 오전 11:21
안영준

문제
a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)
케이크 수 a, c 가 주어졌을 때, 다음을 만족하는 케이크 수 b를 계산하자.
a 🍰 b = c
a, c는 b가 항상 유일하게 존재하도록 주어진다.

입력
첫째 줄에 케이크 수 a를 구성하는 자연수 a.x, a.y, a.z 가 차례대로 주어진다. (1 ≤ a.x, a.y, a.z ≤ 100)
둘째 줄에 케이크 수 c를 구성하는 자연수 c.x, c.y, c.z 가 차례대로 주어진다. (1 ≤ c.x, c.y, c.z ≤ 100)

출력
문제의 조건을 만족하는 b.x, b.y, b.z를 하나의 공백을 사이에 두고 차례대로 출력한다.
b는 1 ≤ b.x, b.y, b.z ≤ 100 이고 반드시 유일하게 존재한다.

"""

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(cx - az, cy // ay, cz - ax)
