# 문자열 분석

"""
2021-01-18 오후 4:51
안영준

문제
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

입력
첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100) 문자열의 길이는 100을 넘지 않는다.

출력
첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.

"""
import sys

while True:
    # 개행문자 무시해서 한줄에 받기
    line = sys.stdin.readline().rstrip('\n')
    upper, lower, space, number = 0, 0, 0, 0
    if not line: break
    for i in line:
        # 대문자인가?
        if i.isupper():
            upper += 1
        # 소문자인가?
        elif i.islower():
            lower += 1
        # 십진수인가?
        elif i.isdigit():
            number += 1
        # 공백인가?
        elif i.isspace():
            space += 1
    sys.stdout.write("{} {} {} {}\n".format(lower, upper, number, space))
