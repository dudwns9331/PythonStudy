# 알파벳 거리

"""
2021-01-23 오후 4:05
안영준

문제
길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 알파벳 거리를 구하는 프로그램을 작성하시오.
두 글자 x와 y 사이의 알파벳 거리를 구하려면, 먼저 각 알파벳에 숫자를 할당해야 한다.
'A'=1, 'B' = 2, ..., 'Z' = 26. 그 다음 y ≥ x인 경우에는 y-x, y < x인 경우에는 (y+26) - x가 알파벳 거리가 된다.
예를 들어, 'B'와 'D' 사이의 거리는 4 - 2 = 2이고, 'D'와 'B' 사이의 거리는 (2+26) - 4 = 24이다.

입력
첫째 줄에 테스트 케이스의 수 (< 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고,
두 단어가 공백으로 구분되어져 있다. 단어의 길이는 4보다 크거나 같고, 20보다 작거나 같으며, 알파벳 대문자로만 이루어져 있다.

출력
각 테스트 케이스 마다 각 글자의 알파벳 거리를 공백으로 구분해 출력한다.

"""
# 65~ 90

test = int(input())

result = list()

for i in range(test):
    String = list(map(str, input().split()))
    for j in range(len(String[0])):
        if ord(String[0][j]) > ord(String[1][j]):
            result.append(ord(String[1][j]) + 26 - ord(String[0][j]))
        else:
            result.append(ord(String[1][j]) - ord(String[0][j]))
    print('Distances: ' + ' '.join(map(str, result)))
    result.clear()
