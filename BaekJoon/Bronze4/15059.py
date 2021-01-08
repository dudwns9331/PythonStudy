# hard choice

"""
2021-01-03 오후 5:07
안영준

문제
식사를 선택하지 못한 승객의 수를 구한다.

입력
첫 번째 줄에는 닭고기, 쇠고기 및 파스타에 사용할 수있는
식사 수를 각각 나타내는 세 개의 정수 C a , B a 및 P a (0 ≤ C a , B a , P a ≤ 100)가 포함됩니다.
두 번째 줄에는 3 개의 정수 C r , B r 및 P r (0 ≤ C r , B r , P r ≤ 100)이 포함되며,
이는 각각 닭고기, 쇠고기 및 파스타에 대해 요청 된 식사 수를 나타냅니다.

출력
식사 선택을 확실히받지 못할 승객 수를 나타내는 정수로 한 줄을 출력합니다.

"""


def cal(bob, son):
    if bob >= son:
        return 0
    else:
        return son - bob


a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

print(cal(a, d) + cal(b, e) + cal(c, f))
