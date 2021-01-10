# 오각형, 오각형, 오각형...

"""
2021-01-10 오후 4:06
안영준

문제
오각형의 각 변에 아래 그림과 같이 점을 찍어 나간다. N단계에서 점의 개수는 모두 몇 개일까?

입력
첫째 줄에 N(1≤N≤10,000,000)이 주어진다.

출력
첫째 줄에 N단계에서 점의 개수를 45678로 나눈 나머지를 출력한다.

"""

N = int(input())

base = 5
d = base + 2
result = base

for i in range(1, N):
    result = base + d
    base = result
    d = d + 3
    result = result % 45678

print(result)
