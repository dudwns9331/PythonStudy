# A + B -5

"""
2021-01-05 오전 9:20
안영준

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
입력의 마지막에는 0 두 개가 들어온다.

출력
각 테스트 케이스마다 A+B를 출력한다.

"""

result = list()

while True:
    [a, b] = map(int, input().split())
    if [a, b] == [0, 0]:
        break
    result.append([a, b])

for i in range(len(result)):
    print(result[i][0] + result[i][1])
