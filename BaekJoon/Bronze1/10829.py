# 이진수변환

"""
2021-02-06 오후 10:17
안영준

문제
자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000,000,000,000)

출력
N을 이진수로 바꿔서 출력한다. 이진수는 0으로 시작하면 안 된다.

"""

number = int(input())
result = format(number, 'b')
print(result)
