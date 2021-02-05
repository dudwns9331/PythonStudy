# 나는 학급회장이다

"""
2021-02-03 오후 11:40
안영준

문제
N명의 학생들이 모인 초등학교 반에서 학급회장 선거를 하려고 한다. 그 중 3명이 회장후보로 나왔고,
이들에 대한 선호도를 N명의 학생들 각각에게 적어내도록 하였다. 세 명의 후보는 후보 1번, 후보 2번, 후보 3번이라 한다.
모든 학생은 3명의 후보 중에서 가장 선호하는 후보에게는 3점, 두 번째로 선호하는 후보에게는
2점, 가장 선호하지 않는 후보에게는 1점을 주어야 한다. 3명의 후보에 대한 한
학생의 선호 점수는 모두 다르며, 1점, 2점, 3점이 정확히 한 번씩 나타나야 한다.
후보의 최종 점수는 학생들로부터 받은 자신의 선호도 점수를 모두 더한 값이 된다.
그러면 3명의 후보 중 가장 큰 점수를 받은 후보가 회장으로 결정된다.
단, 점수가 가장 큰 후보가 여러 명인 경우에는 3점을 더 많이 받은 후보를 회장으로 결정하고,
3점을 받은 횟수가 같은 경우에는 2점을 더 많이 받은 후보를 회장으로 결정한다.
그러나 3점과 2점을 받은 횟수가 모두 동일하면, 1점을 받은 횟수도 같을 수밖에 없어 회장을 결정하지 못하게 된다.
여러분은 선호도 투표를 통해 얻은 세 후보의 점수를 계산한 후, 유일하게 회장이
결정되는 경우에는 회장으로 결정된 후보의 번호(1, 2, 3 중 한 번호)와 최고 점수를 출력하고,
회장을 결정하지 못하는 경우에는 번호 0과 최고 점수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 반의 학생들의 수 N (3 ≤ N ≤ 1,000)이 주어진다.
다음 N개의 각 줄에는 각 학생이 제출한 회장후보 3명에 대한 선호 점수가 주어지는 데,
첫 번째 점수는 후보 1번에 대한 점수이고 두 번째 점수는 후보 2번에 대한 점수이고
세 번째 점수는 후보 3번에 대한 점수이다. 이 세 점수는 서로 다르며, 1, 2, 3이 정확히 한 번씩 나타난다.

출력
학생들의 선호도 투표 결과로부터, 회장이 유일하게 결정되는 경우에는 회장으로
결정된 후보의 번호와 최고 점수를 출력하고, 유일하게 결정할 수 없는 경우에는 0과 최고 점수를 출력한다.

"""


def count_score(a: int):
    if a == 3:
        return '3'
    elif a == 2:
        return '2'
    elif a == 1:
        return '1'


N = int(input())

first = 0
second = 0
third = 0

first_count = list()
second_count = list()
third_count = list()

for i in range(N):
    a = list(map(int, input().split()))

    first += a[0]
    first_count.append(count_score(a[0]))

    second += a[1]
    second_count.append(count_score(a[1]))

    third += a[2]
    third_count.append(count_score(a[2]))

if first > second or first > third:
    print(1, first)
elif second > first or second > third:
    print(2, second)
elif third > first or third > second:
    print(3, third)
elif first == second and first > third:
    if first_count.count('3') > second_count.count('3'):
        print(1, first)
    elif first_count.count('3') < second_count.count('2'):
        print(2, second)
    else:
        print(0, max(first, second, third))
elif third == second and third > first:
    if third_count.count('3') > second_count.count('3'):
        print(3, first)
    elif third_count.count('3') < second_count.count('2'):
        print(2, second)
    else:
        print(0, max(first, second, third))
elif first == third and first > second:
    if first_count.count('3') > third_count.count('3'):
        print(1, first)
    elif first_count.count('3') < third_count.count('2'):
        print(3, second)
    else:
        print(0, max(first, second, third))