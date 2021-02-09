# 마술사 이민혁

"""
2021-02-09 오후 11:05
안영준

문제
유명한 마술사인 이민혁이 사용하는 카드의 뒷 면은 모두 자신이 디자인한 카드이다.
민혁이는 카드 뒷 면 전체를 디자인하지 않고, 왼쪽 위 1/4만 디자인한다.
그 다음 대칭시켜 오른쪽 위를 만들고, 다시 대칭시켜서 아래 부분을 모두 만든다.
이렇게 대칭시켜서 전체를 디자인 한 이후에는, 마술하는데 사용하기 위한 의도된 에러를 넣는다.
에러는 원래 '#'이어야 하는 칸을 '.'로 바꾸거나 '.'이어야 하는 칸을 '#'로 바꾸는 것이다.
왼쪽 위의 디자인과 에러의 위치가 주어졌을 때, 카드 뒷 면 전체 디자인을 구하는 프로그램을 작성하시오.
아래 그림은 민혁이의 카드의 예시이다. (회색 칸은 에러이다)

입력
첫째 줄에 왼쪽 위 부분의 행의 개수 R과 열의 개수 C가 주어진다. (1 ≤ R, C ≤ 50)
다음 R개 줄에는 C개의 문자 '.' 또는 '#'가 주어진다.
마지막 줄에는 에러의 위치 A와 B가 주어진다. (1 ≤ A ≤ 2R, 1 ≤ B ≤ 2C)

출력
카드 뒷 면 전체 디자인을 총 2R개 줄에 걸쳐서 출력한다. 각 줄은 2C개의 문자로 이루어져 있어야 한다.

"""

R, C = map(int, input().split())

card = list()

result_card = list()

for i in range(R):
    card.append(list(input()))

up_list = ''

for i in range(R):
    up_list += (''.join(map(str, card[i])) + ''.join(map(str, card[i][::-1])))
up_list += up_list[::-1]

up = 0
for i in range(up, len(up_list) + up, C * 2):
    result_card.append(list(up_list[up:up + C * 2]))
    up = up + C * 2

a, b = map(int, input().split())

if result_card[a - 1][b - 1] == '.':
    result_card[a - 1][b - 1] = '#'
else:
    result_card[a - 1][b - 1] = '.'

count = 0

for i in result_card:
    print(''.join(map(str, i)))
