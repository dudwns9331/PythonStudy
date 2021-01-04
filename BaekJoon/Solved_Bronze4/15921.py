# 수찬은 마린보이야!!

"""
2021-01-04 오전 10:00
안영준

문제
부산의 자랑! 동래의 희망! 부산 앞바다에서 수영선수의 꿈을 키워온 수찬이는
우리나라의 자랑스런 국가대표 수영선수가 되었다.
수찬이는 인터넷 뉴스를 통해 이번 2020 도쿄 하계올림픽 관련 전문가들의 인터뷰를 찾아보고 있다.
자신을 교수라고 소개한 어떤 전문가에 따르면, 유럽의 유명 대학 연구팀의 연구 결과에 따르면,
통계적으로 어떤 선수가 대회에서 연습과 비슷하게 꾸준한 기량을 뽐낼 수 있는 확률은
(연습 기록들의 평균값) / (연습 기록들 중 하나를 균일한 확률로 뽑을 때의 기댓값) 이라고 한다.
수찬이는 이 기사를 읽고 무릎을 탁(!) 치며 자신의 연습 기록을 가지고 이 확률을 계산해보기로 했다.
 찬이가 꾸준한 기량을 뽐낼 수 있는 확률은 얼마일까?

입력
첫째 줄에 수찬이의 연습 기록의 개수 N이 주어진다. (0 ≤ N ≤ 100)
둘째 줄에 수찬이의 연습 기록 N개가 주어진다. N이 0이면 아무것도 주어지지 않으며 연습 기록은 100 이하의 양의 정수이다.

출력
문제에서 제시한 확률을 소수 셋째 자리에서 반올림하여 소수 둘째 자리까지 출력한다. N이 0이거나 분모가 0인 경우에는 “divide by zero”를 출력한다.

"""

N = int(input())

record = list(map(int, input().split()))

record_set = set(record)
record_set = list(record_set)
record_set.sort()
count = list()

AVG = sum(record) / len(record)

for i in range(len(record_set)):
    count.append(record.count(record_set[i]))

expected = 0
for i in range(len(record_set)):
    expected = expected + record_set[i] * (count[i] / N)

if expected == 0 or N == 0:
    print("divide by zero")
else:
    print("%.2f" % (AVG / expected))

# 문제를 잘 읽고 힌트를  잘 읽자.
n = int(input())
if n == 0:
    print("divide by zero")
else:
    print("1.00")
