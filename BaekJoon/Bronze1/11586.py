# 지영 공주님의 마법 거울

"""
2021-02-03 오전 10:23
안영준

문제
천나라 민호성의 지영 공주님은 매우 아름답다. 공주님 자신도 이 세상 그 누구보다 자신이
아름답다는 것을 알고 있다. 공주님은 자신의 아름다움이 세월의 저편으로 사라지는 것을 매우 두려워한다.
그래서 하루에도 수십 수백 번씩 거울을 보며 자신의 모습이 여전히 아름다운지 확인을 거듭한다.
그러던 어느 날, 세상의 다양한 장면들을 담고 싶었던 공주님의 마법거울은 매일 똑같은 모습만을
비추는 자신의 운명에 좌절하며 앞으로의 운명을 개척하기로 결심했다. 마법거울은 매일 자신의
심리상태에 따라 거울에 비친 공주님의 모습을 좌/우 또는 상/하로 반전시켜 비추기로 한다.
마법거울의 심리상태는 1부터 3까지의 자연수로 표현할 수 있으며, 숫자가 클수록 더 화가 난 상태를 의미한다.
마법거울의 심리상태가 1일 때는 지영 공주님의 모습을 있는 그대로 표현하고, 2일 때는
좌/우로 반전된 모습을, 3일 때는 상/하로 반전된 모습을 표현한다. 정사각형 형태의 마법거울의
크기와 거울에 비친 지영 공주님의 원래 모습, 마법거울의 심리상태가 주어졌을 때, 마법거울에 비친 지영 공주님의 모습을 출력하라.

입력
첫 번째 줄에 정사각형 모양의 마법거울의 크기를 나타내는 자연수 N(2 ≤ N ≤ 100)이 입력된다.
그 다음 N개의 줄에 걸쳐 거울에 비친 지영 공주님의 원래 모습이 각 줄에 N개의 문자로 표현된다.
마법거울은 알파벳 대소문자로만 거울에 비친 상을 표현할 수 있다. 마지막 줄에
마법거울의 심리상태를 나타내는 정수 K(1 ≤ K ≤ 3)가 주어진다.

출력
마법거울의 심리상태에 따라 거울에 비친 지영공주님의 모습을 N×N크기의 정사각형
형태로 출력하라. 반전된 모습은 입력으로 주어진 문자의 위치를 반전시키는 것을 의미한다.

"""

N = int(input())

mirror = list()

for i in range(N):
    mirror.append(list(input()))

K = int(input())

if K == 1:
    for i in mirror:
        print(''.join(map(str, i)))
elif K == 2:
    reverse_mirror = list()
    for i in mirror:
        reverse_mirror.append(i[::-1])
    for i in reverse_mirror:
        print(''.join(map(str, i)))
elif K == 3:
    reverse_mirror = mirror[::-1]
    for i in reverse_mirror:
        print(''.join(map(str, i)))
