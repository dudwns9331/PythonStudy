# 균형잡힌 세상

"""
2021-03-11 오전 8:52
안영준

문제 : https://www.acmicpc.net/problem/4949

"""

while True:
    string = input()
    if string == '.':
        break
    stack = []
    is_ok = True
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                is_ok = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                is_ok = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if is_ok == True and not stack:
        print('yes')
    else:
        print('no')
