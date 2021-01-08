# 네 번째 점

"""
2021-01-07 오후 5:38
안영준

문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.

"""

point_x = list()
point_y = list()

for i in range(3):
    x, y = map(int, input().split())
    point_x.append(x)
    point_y.append(y)

for i in range(3):
    if point_x.count(point_x[i]) == 1:
        x = point_x[i]
    if point_y.count(point_y[i]) == 1:
        y = point_y[i]

print(x, y)
