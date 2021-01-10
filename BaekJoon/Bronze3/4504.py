# 배수 찾기

"""
2021-01-10 오후 3:56
안영준

문제
정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. 다음 줄부터 한 줄에 한 개씩 목록에 들어있는 수가 주어진다. 이 수는 0보다 크고, 10,000보다 작다. 목록은 0으로 끝난다.

출력
목록에 있는 수가 n의 배수인지 아닌지를 구한 뒤 예제 출력처럼 출력한다.

"""

n = int(input())

while True:
    number = int(input())

    if number == 0:
        break
    elif number % n == 0:
        print(f"{number} is a multiple of {n}.")
    else:
        print(f"{number} is NOT a multiple of {n}.")
