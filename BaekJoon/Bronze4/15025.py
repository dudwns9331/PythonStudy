# Judging Moose

"""
2021-01-03 오후 4:48
안영준

문제
황소 무스의 나이를 측정한다.

입력
입력에는 두 개의 정수 ℓ 및 r이있는 단일 행이 포함됩니다. 여기서 0 ≤ ℓ ≤ 20은 왼쪽의 타인 수이고 0 ≤ r ≤ 20은 오른쪽의 타인 수입니다.

출력
무스를 설명하는 한 줄을 출력합니다. 뾰족한 무스의 경우 "Even x"를 출력합니다.
여기서 x는 무스의 점입니다. 뾰족한 무스의 경우 "Odd x"를 출력합니다.
여기서 x는 무스의 점입니다. 무스에 가지가 없으면 "Not a moose"를 출력합니다.

"""

a, b = map(int, input().split())

if a == 0 or b == 0:
    print("Not a moose")
elif a != b:
    result = max(a, b) * 2
    print("Odd %d" % result)
else:
    result = max(a, b) * 2
    print("Even %d" % result)
