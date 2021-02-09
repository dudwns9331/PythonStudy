# Quicksum

"""
2021-02-09 오전 9:52
안영준

문제
이 문제에서 당신은 Quicksum이라고 하는 checksum 알고리즘을 구현해야 한다.
Quicksum 패킷은 오직 대문자와 공백으로 이루어져있다. 그리고 시작과 끝은 항상 대문자이다.
공백은 문자와 섞여있을수 있으며 연속되어서 있을수도 있다.
Quicksum은 각각의 문자의 위치와 문자 값의 합이다. 공백은 0이다.
문자는 고유의 위치값을 가지고 있는데 예를들어 A=1, B=2 ... Z=26이다.
예제 문장은 "ACM" 과 "MID CENTRAL"인데 살펴보면 다음과 같다.
ACM: 1*1  + 2*3 + 3*13 = 46
MID CENTRAL: 1*13 + 2*9 + 3*4 + 4*0 + 5*3 + 6*5 + 7*14 + 8*20 + 9*18 + 10*1 + 11*12 = 650

입력
# 이 들어오기 전까지 계속 입력을 받는다. 각각의 패킷은 한줄에 하나씩 입력이 되며 공백으로 시작되거나 끝나지 않으며, 대문자만 입력이 된다. 패킷의 길이는 1~255자이다.

출력
각각의 패킷에 따라 한줄에 하나씩 Quicksum 을 출력하라.

"""

alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    string = input()
    if string == '#':
        break
    else:
        result = 0
        for i in range(len(string)):
            result += alphabet.index(string[i]) * (i + 1)
        print(result)
