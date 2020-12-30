# 곱셈

"""
2020-12-29 오후 10:50
안영준

입력
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

"""

a = int(input())
b = input()

result = 0
power = 1

for i in range(len(b)):
    result = result + (a * int(b[-i - 1]) * power)
    power = power * 10
    print(a * int(b[-i - 1]))

print(result)
