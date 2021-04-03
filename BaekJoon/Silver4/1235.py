# 학생 번호

"""
2021-04-02 오후 10:55
안영준

문제 : https://www.acmicpc.net/problem/1235
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

student_number = list()

for i in range(eval(input())):
    student_number.append(input())
