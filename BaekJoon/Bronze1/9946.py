# 단어 퍼즐

"""
2021-02-11 오전 10:46
안영준

문제 : https://www.acmicpc.net/problem/9946

"""
count = 1

while True:
    same = True
    a = input()
    b = input()

    if a == b == 'END':
        break

    if len(a) == len(b):
        for i in range(len(a)):
            if a.count(a[i]) != b.count(a[i]):
                same = False
        if same:
            print(f'Case {count}: same')
            count += 1
        else:
            print(f'Case {count}: different')
            count += 1
    else:
        print(f'Case {count}: different')
        count += 1
