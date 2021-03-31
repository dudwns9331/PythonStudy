# 괄호 끼워 넣기

"""
2021-03-30 오후 8:37
안영준

문제 : https://www.acmicpc.net/problem/11899
"""

count = 0

result = True
stack = list()
string = list(input())
for j in string:
    if j == '(':
        stack.append('(')
    else:
        if len(stack) == 0:
            result = False
            count += 1
        else:
            stack.pop()

if len(stack) > 0:
    result = False

print(count + len(stack))
