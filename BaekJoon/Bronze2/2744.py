# 대소문자 바꾸기

"""
2021-01-20 오후 4:09
안영준

문제
영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어의 길이는 최대 100이다.

출력
첫째 줄에 입력으로 주어진 단어에서 대문자는 소문자로, 소문자는 대문자로 바꾼 단어를 출력한다.

"""

String = input()

result = list()

for i in range(len(String)):
    if String[i].islower():
        result.append(String[i].upper())
    else:
        result.append(String[i].lower())

print(''.join(map(str, result)))
