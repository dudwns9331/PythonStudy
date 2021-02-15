# 패리티

"""
2021-02-15 오전 11:16
안영준

문제 : https://www.acmicpc.net/problem/4597

"""

while True:
    string = input()
    if string == "#":
        break
    else:
        count = string.count('1')
        if string[-1] == 'e':
            if count % 2 == 0:
                string = string.replace('e', '0')
            else:
                string = string.replace('e', '1')
        elif string[-1] == 'o':
            if count % 2 == 0:
                string = string.replace('o', '1')
            else:
                string = string.replace('o', '0')
    print(string)
