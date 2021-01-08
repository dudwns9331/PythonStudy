# 적어도 대부분의 배수

"""
2021-01-02 오후 3:12
안영준

문제
다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.
서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 다섯 개의 자연수가 주어진다. 100보다 작거나 같은 자연수이고, 서로 다른 수이다.

출력
첫째 줄에 적어도 대부분의 배수를 출력한다.

"""

number = list(map(int, input().split()))
small = min(number)

while True:
    c = 0
    for i in range(len(number)):
        if small % number[i] == 0:
            c = c + 1

    if c >= 3:
        print(small)
        break

    small = small + 1
