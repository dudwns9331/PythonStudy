# 숫자의 합

"""
2021-01-09 오후 5:45
안영준

문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.

"""

N = int(input())

number = list(input())
result = 0

for i in number:
    result += int(i)

print(result)
