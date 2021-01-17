# 거스름돈

"""
2021-01-17 오후 6:38
안영준

문제
타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고,
언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때,
받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.

입력
입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.

출력
제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.

"""

pay = int(input())
changes = 1000 - pay

count = 0

while True:
    if changes >= 500:
        changes = changes - 500
        count += 1
    elif changes >= 100:
        count += changes // 100
        changes = changes - (changes // 100 * 100)
    elif changes >= 50:
        count += changes // 50
        changes = changes - (changes // 50 * 50)
    elif changes >= 10:
        count += changes // 10
        changes = changes - (changes // 10 * 10)
    elif changes >= 5:
        count += changes // 5
        changes = changes - (changes // 5 * 5)
    else:
        count += changes
        break

print(count)
