# Winning Score

"""
2021-01-04 오전 9:33
안영준

문제
농구 경기에서 모든 득점 활동을 기록합니다.
점수는 3 점 슛, 2 점 필드 골 또는 1 점 자유투로 득점합니다.
두 팀, 즉 사과와 바나나에 대한 이러한 각 유형의 점수를 알고 있습니다.
당신의 임무는 어느 팀이 이겼는지 또는 게임이 동점으로 끝났는지 결정하는 것입니다.

입력
처음 세 줄의 입력은 사과의 점수를 설명하고 다음 세 줄의 입력은 바나나의 점수를 설명합니다.
각 팀의 첫 번째 줄에는 성공한 3 점 슛 수, 두 번째 줄에는 성공한 2 점 필드 골 수,
세 번째 줄에는 성공한 1 점 자유투 횟수가 포함됩니다. 각 숫자는 0에서 100 사이의 정수입니다.

출력
출력은 단일 문자입니다. 사과가 바나나보다 더 많은 점수를 얻은 경우 'A'를 출력합니다.
바나나가 사과보다 더 많은 점수를 얻은 경우 'B'를 출력합니다. 그렇지 않으면 'T'를 출력하여 동점을 나타냅니다.

"""

apple3 = int(input())
apple2 = int(input())
apple1 = int(input())

banana3 = int(input())
banana2 = int(input())
banana1 = int(input())

if banana3 * 3 + banana2 * 2 + banana1 > apple3 * 3 + apple2 * 2 + apple1:
    print("B")
elif banana3 * 3 + banana2 * 2 + banana1 < apple3 * 3 + apple2 * 2 + apple1:
    print("A")
else:
    print("T")
