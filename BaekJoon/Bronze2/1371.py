# 가장 많은 글자

"""
2021-01-24 오후 4:41
안영준

문제
영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.
어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 글의 문장이 주어진다. 글은 최대 5000글자로 구성되어 있고, 공백, 알파벳 소문자,
엔터로만 이루어져 있다. 그리고 적어도 하나의 알파벳이 있다.

출력
첫째 줄에 가장 많이 나온 문자를 출력한다. 여러 개일 경우에는 알파벳 순으로 앞서는 것부터 모두 공백없이 출력한다.


개수가 같을 때 출력하는거 해결 못함 다른 방법으로 해야함.
구글 검색 블로그 참고함!! 다시풀기
"""

String = ""
while True:
    try:
        String += input()
    except:
        break

result = ['a', String.count('a')]
for o in range(98, 123):
    n = String.count(chr(o))
    if n > result[1]:
        result[0] = chr(o)
        result[1] = n
    elif n == result[1]:
        result[0] += chr(o)
print(result[0])
