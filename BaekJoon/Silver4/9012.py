# 괄호

"""
2021-02-24 오후 3:40
안영준

문제 : https://www.acmicpc.net/problem/9012

"""

T = int(input())

for i in range(T):
    result = True
    stack = list()
    string = list(input())
    for j in string:
        if j == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                result = False
            else:
                stack.pop()

    if len(stack) > 0:
        result = False

    if result:
        print('YES')
    else:
        print('NO')
